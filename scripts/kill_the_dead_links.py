import frontmatter
import pathlib
import requests


def populate_file_list(path_list, root):
    for path in root.iterdir():
        if path.is_dir():
            populate_file_list(path_list, path)
        if path.is_file() and path.suffix.lower() in {".md"}:
            path_list.append(path)


def kill_the_dead_links(path):
    print(f"Processing file \"{path}\"..")
    post = frontmatter.load(path)
    if "learning_resources" in post.metadata:
        for resource in post.metadata["learning_resources"]:
            print(f"Requesting URL \"{resource['url']}\"..")
            try:
                response = requests.get(resource["url"], timeout=5)
                response.raise_for_status()
            except:
                print(f"Dead link found: {resource['url']}")
                post.metadata["learning_resources"].remove(resource)
        frontmatter.dump(post, path, sort_keys=False)


def main():
    CONTENTS_ROOT = "../src/topics"
    path_list = []
    populate_file_list(path_list, pathlib.Path(CONTENTS_ROOT).expanduser())
    for path in path_list:
        kill_the_dead_links(path)


if __name__ == "__main__":
    main()
