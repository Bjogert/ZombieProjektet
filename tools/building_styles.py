#!/usr/bin/env python3
"""Prepare a deterministic building style manifest from GeoJSON.

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


def build_manifest(collection, styles, seed=0):
    if collection.get("type") != "FeatureCollection":
        raise ValueError("Expected a GeoJSON FeatureCollection")
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
        results.append({
            "source_id": feature_id,
            "building_type": building_type,
            "name": properties.get("name"),
            "style": choose_style(feature_id, building_type, styles, seed),
            "source_geometry": geometry,
            "status": "design_only_no_game_tiles",
        })
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
    args = parser.parse_args()
    source = json.loads(args.input.read_text(encoding="utf-8"))
    styles = json.loads(args.styles.read_text(encoding="utf-8"))
    result = build_manifest(source, styles, args.seed)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(result['buildings'])} style proposals to {args.output}")


if __name__ == "__main__":
    main()
