set shell := ["cmd.exe", "/d", "/c"]

build:
    uv run mkdocs build --clean --strict

serve:
    uv run mkdocs serve

install:
    uv run pre-commit install

fmt:
    uv run pymarkdown scan ./src

add-frontmatter:
    uv run python3 scripts/add_frontmatter_to_topics.py