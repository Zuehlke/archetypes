build:
    uv run mkdocs build --clean --strict

serve:
    uv run mkdocs serve

install:
    uv run pre-commit install

fmt:
    uv run pymarkdown scan ./src

check-duplicates:
    uv run python3 scripts/check_duplicate_topics.py