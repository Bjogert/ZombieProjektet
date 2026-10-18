"""Build a metric road-only test map; official WorldEd performs game export."""

import argparse
import hashlib
import json
import math
import shutil
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
from tools.build_m0 import SIZE, make_tmx, write_png
from tools.package_m0 import validate_header, validate_cottage_metadata

GRASS = ("blends_natural_01", 16)
ASPHALT = ("blends_street_01", 0)
GRAVEL = ("blends_street_01", 48)


def plan(data):
    if data.get("crs") != "EPSG:3006" or data.get("metres_per_square") != 1:
        raise ValueError("Expected EPSG:3006 at 1:1")
    route = data.get("route", [])
    if not route:
        raise ValueError("Empty road route")
    all_points = []
    previous = None
    distance = 0
    for segment in route:
        points = segment["coordinates"]
        width = segment["width"]
        if len(points) != 2 or not math.isfinite(width) or not 2 <= width <= 16:
            raise ValueError("Invalid segment or road width")
        if any(len(p) != 2 or any(not math.isfinite(v) for v in p) for p in points):
            raise ValueError("Invalid coordinates")
        if previous is not None and math.dist(previous, points[0]) > 0.01:
            raise ValueError("Route must be connected and ordered")
        tags = segment.get("tags", {})
        if tags.get("layer", "0") != "0" or any(
            tags.get(key) not in (None, "no", "false", "0")
            for key in ("bridge", "tunnel")
        ):
            raise ValueError("Grade-separated crossing requires explicit treatment")
        distance += math.dist(*points)
        all_points.extend(points)
        previous = points[-1]
    if (
        math.dist(data["start"], all_points[0]) > 0.01
        or math.dist(data["end"], all_points[-1]) > 0.01
    ):
        raise ValueError("Endpoints do not match route")
    west = math.floor(min(p[0] for p in all_points)) - 150
    north = math.ceil(max(p[1] for p in all_points)) + 150

    def project(p):
        return (p[0] - west, north - p[1])

    roads = {}
    path = []
    for segment in route:
        a, b = map(project, segment["coordinates"])
        path.append(a)
        width = segment["width"]
        r = width / 2
        dx = b[0] - a[0]
        dy = b[1] - a[1]
        den = dx * dx + dy * dy
        if not den:
            continue
        tile = (
            GRAVEL
            if segment.get("surface")
            in ("gravel", "fine_gravel", "compacted", "unpaved", "ground", "dirt")
            else ASPHALT
        )
        for y in range(
            math.floor(min(a[1], b[1]) - r), math.ceil(max(a[1], b[1]) + r) + 1
        ):
            for x in range(
                math.floor(min(a[0], b[0]) - r), math.ceil(max(a[0], b[0]) + r) + 1
            ):
                t = max(
                    0, min(1, ((x + 0.5 - a[0]) * dx + (y + 0.5 - a[1]) * dy) / den)
                )
                if (x + 0.5 - a[0] - t * dx) ** 2 + (
                    y + 0.5 - a[1] - t * dy
                ) ** 2 <= r * r:
                    roads[x, y] = tile
    path.append(project(all_points[-1]))
    width = math.ceil((max(p[0] for p in all_points) - west + 150) / SIZE)
    height = math.ceil((north - min(p[1] for p in all_points) + 150) / SIZE)
    return {
        "roads": roads,
        "path": path,
        "start": tuple(map(math.floor, project(data["start"]))),
        "end": tuple(map(math.floor, project(data["end"]))),
        "width": width,
        "height": height,
        "source_offset": {"west": west, "north": north},
        "distance_m": distance,
    }


def terrain_cells(p):
    """Rasterized road and synthetic pads, shared by road/integration fixtures."""
    cells = {}
    for (x, y), tile in p["roads"].items():
        cells.setdefault((x // SIZE, y // SIZE), {})[y % SIZE * SIZE + x % SIZE] = tile
    # Explicitly synthetic staging pads, independent of source geometry.
    for px, py in [p["start"], p["end"]]:
        for y in range(py - 10, py + 11):
            for x in range(px - 10, px + 11):
                cells.setdefault((x // SIZE, y // SIZE), {})[
                    y % SIZE * SIZE + x % SIZE
                ] = ASPHALT
    return cells


def build(source, output, tiles, game, cell_layers=None):
    data = json.loads(source.read_text(encoding="utf-8"))
    p = plan(data)
    if output.exists():
        raise FileExistsError(output)
    if not (game / "media/newtiledefinitions.tiles").is_file():
        raise FileNotFoundError("Game TileDefs missing")
    # Validate external tiles and replacement cells before creating output.
    make_tmx(tiles, {"0_Floor": [GRASS] * SIZE**2}, [], [GRASS[0], ASPHALT[0]])
    replacements = {}
    for (cx, cy), layers in (cell_layers or {}).items():
        if not (0 <= cx < p['width'] and 0 <= cy < p['height']):
            raise ValueError('Replacement cell outside road extent')
        if any(len(values) != SIZE**2 for values in layers.values()):
            raise ValueError('Replacement layer must cover one authoring cell')
        tilesets = sorted({tile[0] for values in layers.values() for tile in values if tile})
        replacements[cx, cy] = make_tmx(tiles, layers, [], tilesets)
    output.mkdir(parents=True)
    (output / "export").mkdir()
    cells = terrain_cells(p)
    world = ET.Element(
        "world", version="1.0", width=str(p["width"]), height=str(p["height"])
    )
    lots = ET.SubElement(world, "GenerateLots")
    for tag, attrs in [
        ("exportdir", {"path": "export"}),
        ("ZombieSpawnMap", {"path": "roads_ZombieSpawnMap.png"}),
        ("TileDefFolder", {"path": (game / "media").resolve().as_posix()}),
        ("worldOrigin", {"origin": "0,0"}),
    ]:
        ET.SubElement(lots, tag, **attrs)
    for cy in range(p["height"]):
        for cx in range(p["width"]):
            ground = [GRASS] * SIZE**2
            for i, tile in cells.get((cx, cy), {}).items():
                ground[i] = tile
            name = f"road_{cx}_{cy}.tmx"
            (output / name).write_bytes(
                replacements[cx, cy] if (cx, cy) in replacements else
                make_tmx(tiles, {"0_Floor": ground}, [], [GRASS[0], ASPHALT[0]])
            )
            ET.SubElement(world, "cell", x=str(cx), y=str(cy), map=name)
    ET.ElementTree(world).write(
        output / "roads.pzw", encoding="utf-8", xml_declaration=True
    )
    write_png(output / "roads_ZombieSpawnMap.png", p["width"] * 30, p["height"] * 30)
    manifest = {k: v for k, v in p.items() if k != "roads"}
    manifest.update(
        source_sha256=data.get("source_sha256"),
        normalized_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
        attribution=data["attribution"],
        authoring_cells=p["width"] * p["height"],
        road_squares=len(p["roads"]),
    )
    (output / "manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
    print(
        json.dumps(
            {
                k: manifest[k]
                for k in [
                    "distance_m",
                    "width",
                    "height",
                    "authoring_cells",
                    "road_squares",
                    "start",
                    "end",
                ]
            },
            indent=2,
        )
    )


def package(source, output):
    if output.exists():
        raise FileExistsError(output)
    m = json.loads((source / "manifest.json").read_text())
    required = []
    for y in range(math.ceil(m["height"] * SIZE / 256)):
        for x in range(math.ceil(m["width"] * SIZE / 256)):
            for name in [
                f"{x}_{y}.lotheader",
                f"world_{x}_{y}.lotpack",
                f"chunkdata_{x}_{y}.bin",
            ]:
                f = source / "export" / name
                if not f.is_file() or f.stat().st_size == 0:
                    raise FileNotFoundError(f)
                if f.suffix == ".lotheader":
                    validate_header(f)
                required.append(f)
    integrated = m.get('integration')
    if integrated and integrated.get('format') != 'synthetic-roadside-v1':
        raise ValueError('Unsupported integration manifest')
    if integrated:
        cx, cy = integrated['cell']
        ox, oy = integrated['building']['origin']
        hx, hy = (cx * SIZE + ox) // 256, (cy * SIZE + oy) // 256
        validate_cottage_metadata(source / 'export' / f'{hx}_{hy}.lotheader')
    mod_id = 'ZombieProjektetRoadside' if integrated else 'ZombieProjektetRoadTest'
    map_id = 'RoadsideTest' if integrated else 'GetabodaRoadTest'
    title = 'Roadside cottage test' if integrated else 'Getaboda road test'
    description = ('Fictional cottage, garden and driveway beside the road prototype. New save required.'
                   if integrated else '1:1 road corridor toward Agunnaryd. New save required. Provisional widths, plain terrain.')
    mod = output / mod_id
    maps = mod / f"42/media/maps/{map_id}"
    maps.mkdir(parents=True)
    (mod / "common/media/maps").mkdir(parents=True)
    (mod / "common/media/maps/.gitkeep").touch()
    (mod / "42/mod.info").write_text(
        f"name=ZombieProjektet - {title}\nid={mod_id}\ndescription={description}\nversionMin=42.20\n"
    )
    sx, sy = m["start"]
    (maps / "map.info").write_text(
        f"title=ZombieProjektet - {title}\ndescription={description}\nfixed2x=true\nzoomX={sx}\nzoomY={sy}\nzoomS=4\n"
    )
    spawn_x, spawn_y = integrated['spawn'] if integrated else (sx + 5, sy)
    (maps / "spawnpoints.lua").write_text(
        f"function SpawnPoints() return {{ unemployed = {{ {{posX={spawn_x},posY={spawn_y},posZ=0}} }} }} end\n"
    )
    (maps / "objects.lua").write_text("objects = {}\n")
    (mod / "ATTRIBUTION.txt").write_text(
        m["attribution"]
        + "\nhttps://www.openstreetmap.org/copyright\nOpen Database License 1.0. Derived road geometry retains ODbL terms.\nRoad widths, endpoint staging pads and any cottage/driveway/garden placement are provisional fictional design choices.\n",
        encoding="utf-8",
    )
    for f in required:
        shutil.copy2(f, maps / f.name)
    client = mod / "42/media/lua/client"
    client.mkdir(parents=True)
    template = (
        Path(__file__).with_name("road_test_setup.lua").read_text(encoding="utf-8")
    )
    config = f'local TEST_MAP = "{map_id}"\nlocal START_X, START_Y, END_X, END_Y = {sx},{sy},{m["end"][0]},{m["end"][1]}\n'
    (client / "RoadTestSetup.lua").write_text(config + template, encoding="utf-8")
    with zipfile.ZipFile(
        output / (mod_id + '.zip'), "w", zipfile.ZIP_DEFLATED
    ) as archive:
        for f in sorted(mod.rglob("*")):
            if f.is_file():
                info = zipfile.ZipInfo(f.relative_to(output).as_posix())
                info.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(info, f.read_bytes())
    print(
        f"Packaged {len(required)//3} runtime cells; game verification still required."
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["build", "package"])
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--tiles", type=Path)
    parser.add_argument("--game", type=Path)
    args = parser.parse_args()
    if args.action == "build":
        build(args.source, args.output, args.tiles, args.game)
    else:
        package(args.source, args.output)
