"""Register a frozen local building sample without exposing geometry to stdout.

Source refreshes require explicit reconciliation. Official game authoring and
real-building verification are separate from this candidate/measurement register.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import tempfile
import uuid

from tools.building_styles import unique_override_keys

APPEARANCE = ('facade_color', 'facade_material', 'roof_color', 'roof_material',
              'roof_shape', 'storeys', 'height_m', 'deck', 'garden')
FORMAT = 'zombieprojektet-local-building-register-v1'


def decode(data):
    return json.loads(data, object_pairs_hook=unique_override_keys)


def measurements(feature, crs, selection):
    from pyproj import Transformer
    from shapely import get_coordinates, transform
    from shapely.geometry import Point, shape

    geo = feature.get('geometry') or {}
    if geo.get('type') not in ('Polygon', 'MultiPolygon'):
        raise ValueError('Expected polygon geometry')
    g = shape(geo)
    if g.is_empty or not g.is_valid or g.has_z:
        raise ValueError('Invalid, empty or 3D building geometry')
    coords = get_coordinates(g)
    if not all(math.isfinite(float(v)) for row in coords for v in row):
        raise ValueError('Non-finite geometry')
    if crs == 4326:
        if any(not (10 <= x <= 25 and 54 <= y <= 70) for x, y in coords):
            raise ValueError('Outside supported Swedish longitude/latitude extent')
        g = transform(g, Transformer.from_crs(4326, 3006, always_xy=True).transform,
                      interleaved=False)
    if not g.is_valid or g.area <= 0:
        raise ValueError('Invalid projected geometry')
    if g.distance(Point(selection['center'])) > selection['radius_m']:
        raise ValueError('Building outside registered selection')
    # A long spurious polygon must not qualify merely by touching the selection.
    if any(math.dist(p, selection['center']) > selection['radius_m'] + 100
           for p in get_coordinates(g)):
        raise ValueError('Building extends beyond selection allowance')
    rect = g.minimum_rotated_rectangle
    points = list(rect.exterior.coords)
    edges = [(math.dist(a, b), math.degrees(math.atan2(b[0]-a[0], b[1]-a[1])) % 180)
             for a, b in zip(points, points[1:])]
    sides = sorted(length for length, _ in edges)
    direction = min(angle for length, angle in edges if abs(length-sides[-1]) < 1e-7)
    return {'method': 'EPSG:3006 minimum rotated rectangle; not exact wall dimensions',
            'area_m2': round(g.area, 3),
            'rectangle_sides_m': [round(sides[0], 3), round(sides[-1], 3)],
            'rectangle_occupancy': round(g.area/rect.area, 5),
            'long_axis_degrees_from_north': round(direction, 3) % 180}


def build(input_path, source_path, output):
    raw, provenance_bytes = input_path.read_bytes(), source_path.read_bytes()
    source, collection = decode(provenance_bytes), decode(raw)
    required = {'provider', 'release', 'url', 'license', 'attribution', 'crs', 'sha256', 'selection'}
    if not isinstance(source, dict) or set(source) != required:
        raise ValueError('Source metadata must contain the documented fields')
    if any(not isinstance(source[k], str) or not source[k].strip()
           for k in required - {'crs', 'selection'}):
        raise ValueError('Source metadata strings must be nonempty')
    if source['sha256'] != hashlib.sha256(raw).hexdigest():
        raise ValueError('Source hash mismatch')
    if type(source['crs']) is not int or source['crs'] not in (3006, 4326):
        raise ValueError('Only EPSG:3006 and longitude/latitude EPSG:4326 are supported')
    selection = source['selection']
    if not isinstance(selection, dict) or set(selection) != {'center', 'radius_m'}:
        raise ValueError('Selection requires metric center and radius_m')
    center, radius = selection['center'], selection['radius_m']
    if (not isinstance(center, list) or len(center) != 2
        or any(type(v) not in (int, float) or not math.isfinite(v) for v in center)
        or not (0 <= center[0] <= 1000000 and 6000000 <= center[1] <= 8000000)
        or type(radius) not in (int, float) or not math.isfinite(radius) or not 0 < radius <= 1500):
        raise ValueError('Selection must be bounded in Swedish metric coordinates')
    if not isinstance(collection, dict) or collection.get('type') != 'FeatureCollection':
        raise ValueError('Expected a FeatureCollection')
    features = collection.get('features')
    if not isinstance(features, list) or not 1 <= len(features) <= 1000:
        raise ValueError('Register requires 1 to 1000 building candidates')
    candidates = {}
    for feature in features:
        if not isinstance(feature, dict) or feature.get('type') != 'Feature':
            raise ValueError('Invalid feature')
        alias = feature.get('id')
        if not isinstance(alias, str) or not alias.strip() or alias in candidates:
            raise ValueError('Unique nonempty source IDs required')
        candidates[alias] = measurements(feature, source['crs'], selection)
    if output.exists():
        if ((output/'source.geojson').read_bytes() != raw
            or (output/'source.json').read_bytes() != provenance_bytes):
            raise ValueError('Source changed; explicit reconciliation required')
        saved = decode((output/'registry.json').read_bytes())
        if saved.get('format') != FORMAT or saved.get('source_sha256') != source['sha256']:
            raise ValueError('Invalid register identity metadata')
        records = saved.get('buildings', [])
        ids = [b.get('id') for b in records]
        aliases = [b.get('source_alias') for b in records]
        if len(set(ids)) != len(ids) or len(aliases) != len(candidates) or set(aliases) != set(candidates):
            raise ValueError('Register identity mismatch; manual reconciliation required')
        for identifier in ids:
            if str(uuid.UUID(identifier)) != identifier:
                raise ValueError('Invalid project identity')
        if any(b.get('measurements') != candidates[b['source_alias']] for b in records):
            raise ValueError('Derived measurements changed; explicit reconciliation required')
        if not (output/'choices.json').is_file():
            raise ValueError('Missing saved choices; do not reset them silently')
        return {'registered': len(records), 'reused': True}
    records = [{'id': str(uuid.uuid4()), 'source_alias': alias,
                'status': 'source_candidate_unverified', 'building_use': None,
                'geometry': {'file': 'source.geojson', 'feature_id': alias},
                'measurements': candidates[alias],
                'appearance': dict.fromkeys(APPEARANCE), 'observations': []}
               for alias in sorted(candidates)]
    registry = {'format': FORMAT, 'source_sha256': source['sha256'], 'buildings': records}
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.register-', dir=output.parent) as temporary:
        staged = Path(temporary)/'ready'
        staged.mkdir()
        (staged/'source.geojson').write_bytes(raw)
        (staged/'source.json').write_bytes(provenance_bytes)
        (staged/'registry.json').write_text(json.dumps(registry, indent=2)+'\n', encoding='utf-8')
        (staged/'choices.json').write_text('{}\n', encoding='utf-8')
        staged.rename(output)
    return {'registered': len(records), 'reused': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('input', 'source', 'output'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(build(args.input, args.source, args.output)))
    except (OSError, ValueError, TypeError, KeyError) as error:
        parser.error(str(error))
