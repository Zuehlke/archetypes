#!/usr/bin/env python3
"""
Duplicate topic detector.

Checks:
- Duplicate slugs
- Duplicate titles
- Similar titles (fuzzy match)
"""

from pathlib import Path
import yaml
import difflib

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
        frontmatter["_file"] = md_file.name
        topics.append(frontmatter)

    return topics


def normalize_title(t: str):
    """Convert title to comparable simplified form."""
    if not t:
        return ""

    t = t.lower().strip()
    t = t.replace("(", "").replace(")", "")
    t = t.replace("xp", "").replace("tdd", "")
    t = t.replace("-", " ")
    return " ".join(t.split())


def main():
    print(f"🔍 Checking for duplicate topics in: {TOPIC_ROOT}")

    topics = load_all_topics()

    # Maps for checking duplicates
    seen_slugs = {}
    seen_titles = {}

    errors = []

    for t in topics:
        slug = t["_slug"]
        title = t.get("title", "")
        norm_title = normalize_title(title)
        filename = t["_file"]

        # ------------- SLUG DUPLICATES -------------
        if slug in seen_slugs:
            errors.append(
                f"❌ Duplicate slug '{slug}': {filename} and {seen_slugs[slug]}"
            )
        else:
            seen_slugs[slug] = filename

        # ------------- TITLE DUPLICATES -------------
        if norm_title:
            if norm_title in seen_titles:
                errors.append(
                    f"❌ Duplicate title '{title}': {filename} and {seen_titles[norm_title]}"
                )
            else:
                seen_titles[norm_title] = filename

    # ------------- FUZZY MATCHING FOR SIMILAR TITLES -------------
    titles = list(seen_titles.keys())
    for i in range(len(titles)):
        for j in range(i + 1, len(titles)):
            a, b = titles[i], titles[j]
            ratio = difflib.SequenceMatcher(None, a, b).ratio()

            if ratio > 0.80:  # strong similarity threshold
                errors.append(
                    f"⚠️ Possible duplicate/similar topics:\n"
                    f"   - '{a}'\n"
                    f"   - '{b}'\n"
                    f"     similarity={ratio:.2f}"
                )

    # Output
    print("")

    if errors:
        print("\n".join(errors))
        print(f"\n❌ Found {len(errors)} duplicate or similar topic issues.")
    else:
        print("✅ No duplicates detected!")


if __name__ == "__main__":
    main()
