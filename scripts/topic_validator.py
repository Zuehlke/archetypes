#!/usr/bin/env python3
"""
Minimal topic loader / inspector.

Step 1: Just load all topics from src/topics and print:
- slug
- title (if present)
- tags.archetypes
- tags.levels
"""

from pathlib import Path
import yaml

# repo-root/scripts/topic_validator.py → repo-root/src/topics
TOPIC_ROOT = Path(__file__).parent.parent / "src" / "topics"


def load_all_topics():
    topics = []

    for md_file in TOPIC_ROOT.rglob("*.md"):
        text = md_file.read_text(encoding="utf-8")

        if not text.startswith("---"):
            continue

        parts = text.split("---", 2)
        if len(parts) < 3:
            continue

        frontmatter = yaml.safe_load(parts[1]) or {}
        frontmatter["_slug"] = md_file.stem
        topics.append(frontmatter)

    return topics


def main():
    print(f"🔍 Scanning topics in: {TOPIC_ROOT}")
    topics = load_all_topics()
    print(f"Found {len(topics)} topic files\n")

    for t in topics:
        slug = t.get("_slug")
        title = t.get("title", "<no title>")
        tags = t.get("tags", {})
        archetypes = tags.get("archetypes", [])
        levels = tags.get("levels", [])

        print(f"- {slug}")
        print(f"  title: {title}")
        print(f"  archetypes: {archetypes}")
        print(f"  levels: {levels}")
        print()

if __name__ == "__main__":
    main()
