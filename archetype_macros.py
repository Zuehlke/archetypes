"""
Macros for processing archetype and topic frontmatter data.

This module provides MkDocs macros that process YAML frontmatter
to generate structured content for archetypes and topics.
"""

import jsonschema
import json
from pathlib import Path
from typing import Dict, Any
import yaml
from html import escape
import re

TOPIC_ROOT = Path(__file__).parent / "src" / "topics"

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

def filter_topics_by_required_tags(topics, required_tags: dict):
    required_archetypes = set(required_tags.get("archetypes", []))

    def matches(topic):
        topic_archetypes = set(topic.get("tags", {}).get("archetypes", []))
        return required_archetypes.issubset(topic_archetypes)

    return [t for t in topics if matches(t)]

def group_topics_by_level(topics):
    levels_order = ["novice", "advanced-beginner", "competent", "proficient", "expert"]

    grouped = {lvl: [] for lvl in levels_order}

    for topic in topics:
        topic_levels = topic.get("tags", {}).get("levels", [])
        for lvl in topic_levels:
            if lvl in grouped:
                grouped[lvl].append(topic)

    return grouped

def build_level_mapping(skill_stages):
    level_map = {}

    for stage in skill_stages:
        level_name = stage.get("name", "").lower().replace(" ", "-")
        for topic in stage.get("topics", []):
            level_map[topic] = level_name

    return level_map

def pretty_title(topic):
    """
    Returns a clean, human-readable title.
    1. If topic['title'] exists → use it.
    2. Else → slug → convert ('my-topic-name' → 'My Topic Name').
    """
    if "title" in topic and topic["title"]:
        return topic["title"]

    slug = topic.get("_slug", "")
    words = slug.replace("-", " ").split()

    return " ".join(word.capitalize() for word in words)


def define_env(env):
    """
    Define macros for the MkDocs macros plugin.
    
    This function is called by mkdocs-macros-plugin to register
    the available macros.
    """

    @env.macro
    def debug_all_topics():
        topics = load_all_topics()
        lines = ["<ul>"]
        for t in topics:
            slug = t.get("_slug")
            archetypes = t.get("tags", {}).get("archetypes", [])
            levels = t.get("tags", {}).get("levels", [])
            lines.append(f"<li>{slug} — archetypes={archetypes}, levels={levels}</li>")
        lines.append("</ul>")
        return "\n".join(lines)

    @env.macro
    def debug_filtered():
        frontmatter = env.page.meta
        required_tags = frontmatter.get("required_tags", {})

        topics = load_all_topics()
        filtered = filter_topics_by_required_tags(topics, required_tags)

        lines = ["<ul>"]
        for t in filtered:
            slug = t.get("_slug")
            lines.append(f"<li>{slug}</li>")
        lines.append("</ul>")
        return "\n".join(lines)

    @env.macro
    def debug_grouped():
        frontmatter = env.page.meta
        required_tags = frontmatter.get("required_tags", {})

        topics = load_all_topics()
        filtered = filter_topics_by_required_tags(topics, required_tags)
        grouped = group_topics_by_level(filtered)

        lines = []
        for lvl, items in grouped.items():
            lines.append(f"{lvl}: {len(items)} topics")
        return "<br>".join(lines)

    @env.macro
    def render_dynamic_skill_stages():
        """
        Dynamic version of the pretty skill stage UI:
        - Uses tags & archetype skill_stages mapping
        - Builds Mermaid roadmap dynamically
        - Renders expandable <details> sections
        - Pretty titles (no dashes)
        - Correct level order
        """
        try:
            frontmatter = env.page.meta
            required_tags = frontmatter.get("required_tags", {})

            # Load & filter topics
            topics = load_all_topics()
            filtered = filter_topics_by_required_tags(topics, required_tags)

            # Build mapping from archetype's defined levels
            skill_stages = frontmatter.get("skill_stages", [])
            level_map = build_level_mapping(skill_stages)

            # Assign dynamic level to topics
            for topic in filtered:
                slug = topic["_slug"]
                topic["_level"] = level_map.get(slug, "unassigned")

            # Group topics by level
            grouped = {}
            for topic in filtered:
                lvl = topic["_level"]
                grouped.setdefault(lvl, []).append(topic)

            # Correct order for Dreyfus levels
            ORDER = ["novice", "advanced-beginner", "competent", "proficient", "expert", "unassigned"]

            # ---------- MERMAID DIAGRAM ----------
            mermaid = ["```mermaid", "flowchart LR"]
            prev = None

            for level in ORDER:
                items = grouped.get(level, [])
                if not items:
                    continue

                level_name = level.replace("-", " ").title()
                node_id = safe_slug(level).replace("-", "_")

                mermaid.append(
                    f'  {node_id}["{level_name}<br/><small>({len(items)} topics)</small>"]'
                )

                mermaid.append(
                    f'  click {node_id} "#stage-{safe_slug(level)}" "Show {level_name} topics"'
                )

                if prev:
                    mermaid.append(f"  {prev} --> {node_id}")

                prev = node_id

            mermaid.append("```")

            # ---------- DETAILS SECTIONS ----------
            details = []

            for level in ORDER:
                items = grouped.get(level, [])
                if not items:
                    continue

                level_name = level.replace("-", " ").title()
                slug = safe_slug(level)

                details.append(
                    f'<details id="stage-{slug}"><summary><strong>{level_name}</strong> ({len(items)} topics)</summary>'
                )
                details.append("<ul>")

                # Sort items alphabetically by pretty title
                items = sorted(items, key=lambda t: pretty_title(t))

                for topic in items:
                    slug = topic["_slug"]
                    title = escape(pretty_title(topic))
                    details.append(f'<li><a href="../topics/{slug}/">{title}</a></li>')

                details.append("</ul></details>")
                details.append("")

            return "\n".join(mermaid) + "\n\n" + "\n".join(details)

        except Exception as e:
            return f"<!-- Error in render_dynamic_skill_stages: {e} -->"
    
    @env.macro  
    def render_learning_resources() -> str:
        """
        Render learning resources from topic frontmatter.
        
        Uses the current page's frontmatter to generate a formatted
        list of learning resources by type.
        
        Returns:
            str: Formatted markdown for learning resources
        """
        try:
            # Get frontmatter from current page
            frontmatter = env.page.meta
            
            # Validate frontmatter structure  
            validate_topic_schema(frontmatter)
            
            # Get learning resources from frontmatter
            resources = frontmatter.get('learning_resources', [])
            
            if not resources:
                return "<!-- No learning resources defined in frontmatter -->"
            
            # Generate markdown
            result = ["## Learning Resources", ""]
            
            for resource in resources:
                resource_type = resource.get('type', 'unknown')
                title = resource.get('title', 'Untitled Resource')
                url = resource.get('url', '#')
                description = resource.get('description', '')
                
                # Format based on resource type
                if resource_type == 'book':
                    author = resource.get('author', '')
                    if author:
                        line = f"* [{title}]({url}) by {author}"
                    else:
                        line = f"* [{title}]({url})"
                elif resource_type == 'course':
                    is_internal = resource.get('is_internal', False)
                    lock_icon = " :material-lock:" if is_internal else ""
                    line = f"* [{title}]({url}){lock_icon}"
                else:
                    line = f"* [{title}]({url})"
                
                result.append(line)
                
                # Add description if available
                if description:
                    result.append(f"  {description}")
                
                result.append("")  # Empty line between resources
            
            return "\n".join(result)
            
        except Exception as e:
            return f"<!-- Error rendering learning resources: {str(e)} -->"

    @env.macro
    def render_cross_references() -> str:
        """
        Render cross-references from topic frontmatter.
        Resolves the REAL location of each referenced topic and creates a correct relative link.
        """
        try:
            frontmatter = env.page.meta
            validate_topic_schema(frontmatter)

            cross_refs = frontmatter.get('cross_references', [])
            if not cross_refs:
                return "<!-- No cross-references defined in frontmatter -->"

            result = ["## Related Topics", ""]

            topics_root = Path("src/topics")
            current_page_dir = Path(env.page.file.src_path).parent

            for ref in cross_refs:
                title = topic_slug_to_title(ref)

                # Find actual file
                matches = list(topics_root.rglob(f"{ref}.md"))

                if matches:
                    # Compute relative path from current page
                    real_path = matches[0].relative_to(current_page_dir)
                    link = f"[{title}]({real_path})"
                else:
                    # Fallback to same-folder link (safe fallback)
                    link = f"[{title}](./{ref}.md)"

                result.append(f"* {link}")

            result.append("")
            return "\n".join(result)

        except Exception as e:
            return f"<!-- Error rendering cross-references: {str(e)} -->"


    @env.macro
    def debug_topic_pipeline():
        """
        Display a full debugging panel showing:
        - how many topics were loaded
        - their tags
        - their dynamic mapped level
        - whether they pass required_tags filtering
        """
        try:
            frontmatter = env.page.meta
            required_tags = frontmatter.get("required_tags", {})
            skill_stages = frontmatter.get("skill_stages", [])

            # 1. Load all topics
            topics = load_all_topics()

            # 2. Level mapping
            level_map = build_level_mapping(skill_stages)

            # 3. Apply filters
            filtered = filter_topics_by_required_tags(topics, required_tags)

            lines = []
            lines.append("## 🔍 Topic Pipeline Debug")
            lines.append("")
            lines.append(f"**Total Topics Loaded:** {len(topics)}")
            lines.append(f"**Topics Matching required_tags:** {len(filtered)}")
            lines.append("---")

            for t in topics:
                slug = t["_slug"]
                tags = t.get("tags", {})
                mapped = level_map.get(slug, "unassigned")
                passes = slug in [f["_slug"] for f in filtered]

                lines.append(f"### {slug}")
                lines.append(f"- **tags:** {tags}")
                lines.append(f"- **mapped_level:** `{mapped}`")
                lines.append(f"- **passes filtering:** `{passes}`")
                lines.append("")

            return "\n".join(lines)

        except Exception as e:
            return f"<!-- Error in debug_topic_pipeline: {str(e)} -->"



def topic_slug_to_title(slug: str) -> str:
    """
    Convert a topic slug to a human-readable title.
    
    Args:
        slug: Topic slug (e.g., 'version-control-systems')
        
    Returns:
        str: Human-readable title (e.g., 'Version Control Systems')
    """
    # Convert slug to title case
    words = slug.replace('-', ' ').split()
    title_words = []
    
    for word in words:
        # Handle common abbreviations
        if word.lower() in ['api', 'css', 'html', 'http', 'tls', 'tcp', 'ip', 'dns']:
            title_words.append(word.upper())
        elif word.lower() in ['tdd']:
            title_words.append('TDD')
        else:
            title_words.append(word.capitalize())
    
    return ' '.join(title_words)


def validate_archetype_schema(frontmatter: Dict[str, Any]) -> None:
    """
    Validate archetype frontmatter against JSON schema.
    
    Args:
        frontmatter: The frontmatter data to validate
        
    Raises:
        jsonschema.ValidationError: If frontmatter is invalid
    """
    try:
        # Load schema files
        schema_dir = Path(__file__).parent / "schemas"
        
        # Load common schema for references
        with open(schema_dir / "common.schema.json", 'r') as f:
            common_schema = json.load(f)
        
        # Load archetype schema
        with open(schema_dir / "archetype.schema.json", 'r') as f:
            archetype_schema = json.load(f)
        
        # Create resolver for schema references
        resolver = jsonschema.RefResolver(
            base_uri=schema_dir.as_uri() + "/",
            referrer=archetype_schema,
            store={
                "common.schema.json": common_schema
            }
        )
        
        # Validate frontmatter
        jsonschema.validate(
            instance=frontmatter,
            schema=archetype_schema,
            resolver=resolver
        )
        
    except FileNotFoundError as e:
        # Schema files not found - skip validation for now
        pass
    except jsonschema.ValidationError as e:
        # Re-raise validation errors
        raise e
    except Exception as e:
        # Log other errors but don't break the build
        print(f"Warning: Schema validation failed: {str(e)}")


def validate_topic_schema(frontmatter: Dict[str, Any]) -> None:
    """
    Validate topic frontmatter against JSON schema.
    
    Args:
        frontmatter: The frontmatter data to validate
        
    Raises:
        jsonschema.ValidationError: If frontmatter is invalid
    """
    try:
        # Load schema files
        schema_dir = Path(__file__).parent / "schemas"
        
        # Load common schema for references
        with open(schema_dir / "common.schema.json", 'r') as f:
            common_schema = json.load(f)
        
        # Load topic schema
        with open(schema_dir / "topic.schema.json", 'r') as f:
            topic_schema = json.load(f)
        
        # Create resolver for schema references
        resolver = jsonschema.RefResolver(
            base_uri=schema_dir.as_uri() + "/",
            referrer=topic_schema,
            store={
                "common.schema.json": common_schema
            }
        )
        
        # Validate frontmatter
        jsonschema.validate(
            instance=frontmatter,
            schema=topic_schema,
            resolver=resolver
        )
        
    except FileNotFoundError as e:
        # Schema files not found - skip validation for now
        pass
    except jsonschema.ValidationError as e:
        # Re-raise validation errors
        raise e
    except Exception as e:
        # Log other errors but don't break the build
        print(f"Warning: Schema validation failed: {str(e)}")