"""Extract one bounded corridor from a registered local OSM PBF. No network I/O.

Raw and normalized geometry stays in local files; console output is aggregate
status only. WorldEd export, gameplay verification and distribution are separate.
"""
import argparse
from collections import Counter
import hashlib
import heapq
import importlib.metadata
import json
import math
from pathlib import Path

CLASSES = {'primary', 'secondary', 'tertiary', 'unclassified', 'residential',
           'living_street', 'service', 'road', 'primary_link', 'secondary_link',
           'tertiary_link', 'motorway', 'trunk', 'motorway_link', 'trunk_link'}
ACCESS = ('motorcar', 'motor_vehicle', 'vehicle', 'access')
GRAVEL = {'gravel', 'fine_gravel', 'compacted', 'unpaved', 'ground', 'dirt'}
FALSE = {None, 'no', 'false', '0'}


def eligibility(tags):
    if tags.get('highway') not in CLASSES or tags.get('area') == 'yes':
        return 'road_class', 0
    if tags.get('layer', '0') != '0' or any(tags.get(k) not in FALSE for k in ('bridge', 'tunnel', 'ford')):
        return 'unsupported_crossing', 0
    if any(k.startswith(ACCESS + ('oneway',)) and ':' in k for k in tags):
        return 'conditional_or_directional_access', 0
    access = next((tags[k] for k in ACCESS if k in tags), None)
    if access not in (None, 'yes', 'designated', 'permissive'):
        return 'access', 0
    implied_oneway = tags.get('junction') == 'roundabout' or tags.get('highway') == 'motorway'
    direction = tags.get('oneway', 'yes' if implied_oneway else 'no')
    if direction not in ('yes', 'true', '1', '-1', 'no', 'false', '0'):
        return 'unknown_direction', 0
    return None, -1 if direction == '-1' else 0 if direction in ('no', 'false', '0') else 1


def route(ways, start, end, max_snap, bounds=None):
    points, graph, records, excluded = {}, {}, {}, Counter()
    if not math.isfinite(max_snap) or max_snap <= 0:
        raise ValueError('Invalid maximum snap distance')
    for position in (start, end):
        if len(position) != 2 or not all(math.isfinite(v) for v in position):
            raise ValueError('Invalid endpoint')
        if bounds and not (bounds[0] <= position[0] <= bounds[2] and bounds[1] <= position[1] <= bounds[3]):
            raise ValueError('Endpoint outside registered selection')
    for way in sorted(ways, key=lambda w: w['id']):
        wid, ids, coordinates, tags = way['id'], way['nodes'], way['coordinates'], way['tags']
        if wid in records:
            raise ValueError('Duplicate source way ID')
        records[wid] = way
        if len(ids) != len(coordinates) or len(ids) < 2:
            raise ValueError('Missing road node locations')
        for node, p in zip(ids, coordinates):
            if len(p) != 2 or not all(math.isfinite(v) for v in p):
                raise ValueError('Invalid road node location')
            p = tuple(p)
            if node in points and points[node] != p:
                raise ValueError('Conflicting source node location')
            points[node] = p
        reason, direction = eligibility(tags)
        if reason:
            excluded[reason] += 1
            continue
        for a, b in zip(ids, ids[1:]):
            if bounds and any(not (bounds[0] <= points[n][0] <= bounds[2]
                                  and bounds[1] <= points[n][1] <= bounds[3]) for n in (a, b)):
                continue
            length = math.dist(points[a], points[b])
            if not length:
                continue
            graph.setdefault(a, [])
            graph.setdefault(b, [])
            if direction >= 0:
                graph[a].append((b, wid, length))
            if direction <= 0:
                graph[b].append((a, wid, length))
    if not graph:
        raise ValueError('No eligible road network')
    first, last = (min(graph, key=lambda n: (math.dist(points[n], p), n)) for p in (start, end))
    snaps = [math.dist(points[first], start), math.dist(points[last], end)]
    if max(snaps) > max_snap:
        raise ValueError('Endpoint snap exceeds registered limit')
    if first == last:
        raise ValueError('Endpoints must snap to distinct nodes')
    distances, parent, queue = {first: 0}, {}, [(0, first)]
    while queue:
        cost, node = heapq.heappop(queue)
        if cost != distances[node]:
            continue
        if node == last:
            break
        for nxt, wid, length in sorted(graph[node]):
            new = cost + length
            if new < distances.get(nxt, math.inf):
                distances[nxt], parent[nxt] = new, (node, wid)
                heapq.heappush(queue, (new, nxt))
    if last not in distances:
        raise ValueError('No connected eligible route between endpoints')
    chain, node = [], last
    while node != first:
        prev, wid = parent[node]
        chain.append((prev, node, wid))
        node = prev
    result, missing_access, missing_surface = [], 0, 0
    for a, b, wid in reversed(chain):
        tags = records[wid]['tags']
        missing_access += not any(k in tags for k in ACCESS)
        missing_surface += 'surface' not in tags
        result.append({'id': f'osm/way/{wid}/{a}-{b}', 'way_id': wid,
                       'coordinates': [points[a], points[b]],
                       'width': 5 if tags.get('surface') in GRAVEL else 7,
                       'surface': tags.get('surface'), 'width_status': 'provisional',
                       'tags': {k: tags[k] for k in sorted(tags) if k in {
                           'name', 'ref', 'highway', 'surface', 'width', 'junction', 'oneway',
                           'bridge', 'tunnel', 'layer', 'ford', *ACCESS}}})
    return {'crs': 'EPSG:3006', 'metres_per_square': 1, 'route': result,
            'start': points[first], 'end': points[last], 'distance_m': distances[last],
            'snap_distances_m': snaps, 'excluded_ways': dict(sorted(excluded.items())),
            'uncertainties': {'segments_missing_access': missing_access,
                              'segments_missing_surface': missing_surface,
                              'widths': 'All widths are provisional design choices.',
                              'coverage': 'Source completeness and real-world access are unverified.',
                              'routing_scope': 'Way tags and shared nodes only; node barriers and turn-restriction relations are not evaluated.'}}


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def validate_registry(registry):
    for key in ('dataset_id', 'url', 'snapshot', 'sha256', 'license', 'attribution'):
        if not isinstance(registry.get(key), str) or not registry[key].strip():
            raise ValueError('Incomplete source registration')
    if registry['license'] != 'ODbL-1.0' or not registry['url'].startswith('https://'):
        raise ValueError('Unsupported source registration')
    if len(registry['sha256']) != 64 or any(c not in '0123456789abcdef' for c in registry['sha256']):
        raise ValueError('Invalid registered SHA-256')
    ids = registry.get('place_node_ids', [])
    if len(ids) != 2 or any(type(i) != int or i <= 0 for i in ids) or ids[0] == ids[1]:
        raise ValueError('Register two distinct place-node IDs')
    box = registry.get('bounds_epsg3006', [])
    if len(box) != 4 or not all(math.isfinite(v) for v in box) or not (
            0 < box[2] - box[0] <= 30000 and 0 < box[3] - box[1] <= 30000):
        raise ValueError('Selection must be bounded to at most 30km per axis')
    if not 0 < registry.get('max_snap_m', 0) <= 200:
        raise ValueError('Endpoint snap limit must be between 0 and 200m')


def extract(source, registry_path, output):
    if output.exists():
        raise FileExistsError(output)
    registry_bytes = registry_path.read_bytes()
    registry = json.loads(registry_bytes)
    validate_registry(registry)
    source_hash = digest(source)
    if source_hash != registry['sha256']:
        raise ValueError('Source checksum differs from registered snapshot')
    # Optional libraries are loaded only by the local PBF command.
    import osmium
    from pyproj import Transformer
    project = Transformer.from_crs('EPSG:4326', 'EPSG:3006', always_xy=True).transform
    places, ways = {}, []
    incomplete = Counter()
    bounds = registry['bounds_epsg3006']

    class Reader(osmium.SimpleHandler):
        def node(self, node):
            if node.id in registry['place_node_ids']:
                if not node.tags.get('place') or not node.location.valid():
                    raise ValueError('Registered anchor is not a located place node')
                places[node.id] = project(node.location.lon, node.location.lat)

        def way(self, way):
            if way.tags.get('highway') not in CLASSES:
                return
            coordinates = [project(n.lon, n.lat) if n.location.valid() else None for n in way.nodes]
            if None in coordinates:
                near = any(p is not None and bounds[0] <= p[0] <= bounds[2]
                           and bounds[1] <= p[1] <= bounds[3] for p in coordinates)
                # Never join across missing locations or route a partial way.
                # Missing extent is a documented coverage gap, including locally.
                incomplete['near_selection' if near else 'outside_known_selection'] += 1
                return
            if not any(bounds[0] <= x <= bounds[2] and bounds[1] <= y <= bounds[3]
                       for x, y in coordinates):
                return
            ways.append({'id': way.id, 'nodes': [n.ref for n in way.nodes],
                         'coordinates': coordinates, 'tags': dict(way.tags)})

    Reader().apply_file(str(source), locations=True)
    if set(places) != set(registry['place_node_ids']):
        raise ValueError('Registered place nodes missing from source')
    start, end = (places[i] for i in registry['place_node_ids'])
    result = route(ways, start, end, registry['max_snap_m'], bounds)
    result['uncertainties']['incomplete_ways_excluded'] = dict(sorted(incomplete.items()))
    result.update(source_sha256=source_hash, attribution=registry['attribution'])
    # Catch modification during a long read before committing any derived output.
    if digest(source) != source_hash:
        raise ValueError('Source changed during extraction')
    content = (json.dumps(result, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    provenance = {'format': 'local-osm-corridor-v1', 'source': registry,
                  'registry_sha256': hashlib.sha256(registry_bytes).hexdigest(), 'source_sha256': source_hash,
                  'output_sha256': hashlib.sha256(content).hexdigest(),
                  'libraries': {k: importlib.metadata.version(k) for k in ('osmium', 'pyproj')},
                  'distance_m': result['distance_m'], 'segments': len(result['route']),
                  'way_ids': sorted({s['way_id'] for s in result['route']}),
                  'snap_distances_m': result['snap_distances_m'],
                  'uncertainties': result['uncertainties'], 'excluded_ways': result['excluded_ways']}
    output.mkdir(parents=True)
    (output / 'corridor.json').write_bytes(content)
    (output / 'provenance.json').write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"Local corridor extracted: {len(result['route'])} segments, {result['distance_m']:.2f}m. "
          'Raw geometry retained locally; source completeness and game behavior unverified.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('source', 'registry', 'output'):
        parser.add_argument('--' + key, type=Path, required=True)
    args = parser.parse_args()
    try:
        extract(args.source, args.registry, args.output)
    except (OSError, ValueError, KeyError, ImportError) as error:
        parser.error(str(error))
