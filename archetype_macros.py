"""
Macros for processing archetype and topic frontmatter data.

This module provides MkDocs macros that process YAML frontmatter
to generate structured content for archetypes and topics.
"""

import jsonschema
import json
import re
from pathlib import Path
from typing import Dict, Any
from html import escape

def safe_slug(value: str) -> str:
    """
    Generate a safe HTML ID / anchor slug.
    Rules:
    - lowercase
    - replace spaces with hyphens
    - allow only letters, digits and hyphens
    - ensure it starts with a letter (prepend 's-' if needed)
    """
    slug = value.lower()
    slug = slug.replace(" ", "-")

    slug = re.sub(r"[^a-z0-9\-]", "", slug)

    if not slug or not slug[0].isalpha():
        slug = f"s-{slug}"

    return slug


def define_env(env):
    """
    Define macros for the MkDocs macros plugin.
    """

    @env.macro
    def render_skill_stages(show_topics: bool = True) -> str:
        """
        Render skill stages as a Mermaid flowchart with optional expandable topic lists.
        Creates a horizontal flowchart showing the progression through skill stages,
        with each stage displaying the number of topics. When show_topics is True,
        also generates HTML details elements below the chart with clickable topic links.
        Args:
            show_topics (bool): If True, includes expandable topic lists below the roadmap.
                If False, only renders the Mermaid flowchart. Defaults to True.
        Returns:
            str: Formatted markdown containing:
                - A Mermaid flowchart diagram
                - HTML details/summary elements with topic links (if show_topics=True)
        Expected frontmatter structure:
            frontmatter = env.page.meta
            {
                "skill_stages": [
                    {
                        "name": str,
                        "topics": [str, ...]  # topic slugs
                    },
                    ...
                ],
                ...
            }
        Raises:
            Exception: Any exception during rendering is captured and returned as an HTML comment.
        """
        try:
            frontmatter = env.page.meta
            validate_archetype_schema(frontmatter)

            stages = frontmatter.get("skill_stages", [])
            if not stages:
                return "<!-- No skill stages defined -->"

            # --- Mermaid roadmap ---
            mermaid = ["```mermaid", "flowchart LR"]
            prev = None

            for stage in stages:
                name_raw = stage["name"]
                name = escape(name_raw, quote=True)
                node_id = safe_slug(name_raw).replace("-", "_")
                slug = safe_slug(name_raw)
                count = len(stage.get("topics", []))

                # name is already HTML-escaped, including quotes
                mermaid.append(f'  {node_id}["{name}<br/><small>({count} topics)</small>"]')
                mermaid.append(f'  click {node_id} "#stage-{slug}" "Show {name} topics"')

                if prev:
                    mermaid.append(f"  {prev} --> {node_id}")

                prev = node_id

            mermaid.append("```")

            # Skip expandable details if not requested
            if not show_topics:
                return "\n".join(mermaid)

            # --- Expandable HTML details per stage ---
            details = []

            for stage in stages:
                name_raw = stage["name"]
                name = escape(name_raw)
                slug = safe_slug(name_raw)

                topics = stage.get("topics", [])
                count = len(topics)

                details.append(
                    f'<details id="stage-{slug}"><summary><strong>{name}</strong> ({count} topics)</summary>'
                )
                details.append("<ul>")

                for topic in topics:
                    # topic slug is safe for URLs — do NOT escape it
                    title = escape(topic_slug_to_title(topic))
                    details.append(
                        f'<li><a href="../topics/{topic}/">{title}</a></li>'
                    )

                details.append("</ul></details>")
                details.append("")

            return "\n".join(mermaid) + "\n\n" + "\n".join(details)

        except Exception as e:
            return f"<!-- Error rendering skill stages: {str(e)} -->"

    @env.macro
    def render_learning_resources() -> str:
        """
        Render learning resources from topic frontmatter.
        """
        try:
            frontmatter = env.page.meta
            validate_topic_schema(frontmatter)

            resources = frontmatter.get("learning_resources", [])
            if not resources:
                return "<!-- No learning resources defined in frontmatter -->"

            result = ["## Learning Resources", ""]

            for resource in resources:
                resource_type = resource.get("type", "unknown")
                title = escape(resource.get("title", "Untitled Resource"))
                url = resource.get("url", "#")  # URLs must remain raw
                description = escape(resource.get("description", ""))

                if resource_type == "book":
                    author = escape(resource.get("author", ""))
                    if author:
                        line = f"* [{title}]({url}) by {author}"
                    else:
                        line = f"* [{title}]({url})"

                elif resource_type == "course":
                    is_internal = resource.get("is_internal", False)
                    lock_icon = " :material-lock:" if is_internal else ""
                    line = f"* [{title}]({url}){lock_icon}"

                else:
                    line = f"* [{title}]({url})"

                result.append(line)

                if description:
                    result.append(f"  {description}")

                result.append("")

            return "\n".join(result)

        except Exception as e:
            return f"<!-- Error rendering learning resources: {str(e)} -->"

    @env.macro
    def render_cross_references() -> str:
        """
        Render cross-references from topic frontmatter.
        """
        try:
            frontmatter = env.page.meta
            validate_topic_schema(frontmatter)

            cross_refs = frontmatter.get("cross_references", [])
            if not cross_refs:
                return "<!-- No cross-references defined in frontmatter -->"

            result = ["## Related Topics", ""]

            for ref in cross_refs:
                title = escape(topic_slug_to_title(ref))
                result.append(f"* [{title}](./{ref}.md)")

            result.append("")
            return "\n".join(result)

        except Exception as e:
            return f"<!-- Error rendering cross-references: {str(e)} -->"


def topic_slug_to_title(slug: str) -> str:
    """
    Convert a topic slug to a human-readable title.
    """
    words = slug.replace("-", " ").split()
    title_words = []

    for word in words:
        if word.lower() in ["api", "css", "html", "http", "tls", "tcp", "ip", "dns"]:
            title_words.append(word.upper())
        elif word.lower() == "tdd":
            title_words.append("TDD")
        else:
            title_words.append(word.capitalize())

    return " ".join(title_words)


def validate_archetype_schema(frontmatter: Dict[str, Any]) -> None:
    try:
        schema_dir = Path(__file__).parent / "schemas"

        with open(schema_dir / "common.schema.json", "r") as f:
            common_schema = json.load(f)

        with open(schema_dir / "archetype.schema.json", "r") as f:
            archetype_schema = json.load(f)

        resolver = jsonschema.RefResolver(
            base_uri=schema_dir.as_uri() + "/",
            referrer=archetype_schema,
            store={"common.schema.json": common_schema}
        )

        jsonschema.validate(
            instance=frontmatter,
            schema=archetype_schema,
            resolver=resolver
        )

    except FileNotFoundError:
        print("Warning: Schema file not found during archetype schema validation.")
    except jsonschema.ValidationError:
        raise
    except Exception as e:
        print(f"Warning: Schema validation failed: {str(e)}")


def validate_topic_schema(frontmatter: Dict[str, Any]) -> None:
    try:
        schema_dir = Path(__file__).parent / "schemas"

        with open(schema_dir / "common.schema.json", "r") as f:
            common_schema = json.load(f)

        with open(schema_dir / "topic.schema.json", "r") as f:
            topic_schema = json.load(f)

        resolver = jsonschema.RefResolver(
            base_uri=schema_dir.as_uri() + "/",
            referrer=topic_schema,
            store={"common.schema.json": common_schema}
        )

        jsonschema.validate(
            instance=frontmatter,
            schema=topic_schema,
            resolver=resolver
        )
        
    except FileNotFoundError as e:
        print(f"Warning: Schema file not found: {str(e)}")
    except jsonschema.ValidationError:
        raise
    except Exception as e:
        print(f"Warning: Schema validation failed: {str(e)}")
