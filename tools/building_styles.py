#!/usr/bin/env python3
"""Prepare a deterministic building style manifest from GeoJSON and optional overrides.

Does NOT generate PZ map files, game textures or tiles.
The sample input is fictional; it is NOT georeferenced real-world data.
"""
import argparse
import hashlib
import json
from pathlib import Path


def choose_style(feature_id, building_type, styles, seed=0):
    choices = styles.get("building_styles", {}).get(building_type)
    if not choices:
        choices = styles["default_styles"]
    digest = hashlib.sha256(f"{seed}:{feature_id}".encode("utf-8")).digest()
    return choices[int.from_bytes(digest[:8], "big") % len(choices)]


def unique_override_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate override key: {key}")
        result[key] = value
    return result


def build_manifest(collection, styles, seed=0, overrides=None):
    if collection.get("type") != "FeatureCollection":
        raise ValueError("Expected a GeoJSON FeatureCollection")
    if overrides is None:
        overrides = {}
    if not isinstance(overrides, dict):
        raise ValueError("Overrides must be an object keyed by stable building ID")
    known_styles = set(styles["default_styles"])
    for choices in styles.get("building_styles", {}).values():
        known_styles.update(choices)
    for feature_id, override in overrides.items():
        if not isinstance(feature_id, str):
            raise ValueError("Override IDs must be strings")
        if not isinstance(override, dict) or set(override) != {"style"}:
            raise ValueError(f"Override for {feature_id} must contain only a style field")
        style = override["style"]
        if not isinstance(style, str):
            raise ValueError(f"Override style for {feature_id} must be a string")
        if style not in known_styles:
            raise ValueError(f"Unknown style for {feature_id}: {style}")
    results = []
    seen = set()
    for feature in collection.get("features", []):
        geometry = feature.get("geometry") or {}
        if geometry.get("type") not in ("Polygon", "MultiPolygon"):
            continue
        properties = feature.get("properties") or {}
        building_type = str(properties.get("building") or "").strip().lower()
        if not building_type or building_type == "no":
            continue
        feature_id = feature.get("id")
        if feature_id is None:
            raise ValueError("Building feature without a stable feature ID")
        feature_id = str(feature_id)
        if feature_id in seen:
            raise ValueError(f"Duplicate building ID: {feature_id}")
        seen.add(feature_id)
        style = choose_style(feature_id, building_type, styles, seed)
        if feature_id in overrides:
            style = overrides[feature_id]["style"]
        results.append({
            "source_id": feature_id,
            "building_type": building_type,
            "name": properties.get("name"),
            "style": style,
            "source_geometry": geometry,
            "status": "design_only_no_game_tiles",
        })
    unmatched = set(overrides) - seen
    if unmatched:
        raise ValueError(f"Unmatched override IDs: {', '.join(sorted(unmatched))}")
    results.sort(key=lambda obj: obj["source_id"])
    return {"format": "zombieprojektet-building-style-manifest-v0", "buildings": results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--styles",
        default=Path(__file__).resolve().parents[1] / "config" / "house_styles.json",
        type=Path,
    )
    parser.add_argument("--seed", default=0, type=int)
    parser.add_argument("--overrides", type=Path, help="JSON style overrides keyed by stable building ID")
    args = parser.parse_args()
    try:
        for path in (args.input, args.styles, args.overrides):
            if path is not None and (
                args.output.resolve() == path.resolve()
                or (args.output.exists() and args.output.samefile(path))
            ):
                raise ValueError(f"Output must not overwrite an input file: {path}")
        source = json.loads(args.input.read_text(encoding="utf-8"))
        styles = json.loads(args.styles.read_text(encoding="utf-8"))
        overrides = {}
        if args.overrides is not None:
            overrides = json.loads(
                args.overrides.read_text(encoding="utf-8"), object_pairs_hook=unique_override_keys
            )
            if not isinstance(overrides, dict):
                raise ValueError("Overrides must be an object keyed by stable building ID")
        result = build_manifest(source, styles, args.seed, overrides)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(result['buildings'])} style proposals to {args.output}")


if __name__ == "__main__":
    main()
