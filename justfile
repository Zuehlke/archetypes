build: clean
    uv run mkdocs build

serve:
    uv run mkdocs serve

clean:
    rm -rf ./docs/*