#!/usr/bin/env python3
"""Validate the human HTML overview against its Markdown companion.

The HTML is a static, hand-designed publication artifact. The Markdown file is
the editable overview. This MVP only checks that the HTML reflects its core
paragraphs, not a full Markdown renderer; don't claim automatic synchronization.
"""
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "HUMAN_OVERVIEW.md"
HTML = ROOT / "docs" / "PROJECT_OVERVIEW.html"

def check():
    source = SOURCE.read_text(encoding="utf-8")
    html = HTML.read_text(encoding="utf-8")
    assertions = [
        ("Getaboda", "Getaboda"),
        ("Build 42", "Build 42"),
        ("GitHub", "GitHub"),
        ("1990s", "1990s"),
        ("your comment", 'id="comment"'),
    ]
    failures = [title for title, token in assertions if title not in source or token not in html]
    if failures:
        raise SystemExit("HTML/Markdown overview out of sync: " + ", ".join(failures))
    print("Human overview cross-check OK (core markers only).")
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Validate marker parity")
    args = parser.parse_args()
    if not args.check:
        print("HTML is a manually maintained presentation for now; validating content markers.")
    check()
