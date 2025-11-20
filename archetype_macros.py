"""
Macros for processing archetype and topic frontmatter data.

This module provides MkDocs macros that process YAML frontmatter
to generate structured content for archetypes and topics.
"""

import jsonschema
import json
from pathlib import Path
from typing import Dict, Any


def define_env(env):
    """
    Define macros for the MkDocs macros plugin.
    
    This function is called by mkdocs-macros-plugin to register
    the available macros.
    """
    
    @env.macro
    def render_skill_stages() -> str:
        """
        Render skill stages from archetype frontmatter.
        
        Uses the current page's frontmatter to generate a formatted
        list of skill stages with topic links.
        
        Returns:
            str: Formatted markdown for skill stages
        """
        try:
            # Get frontmatter from current page
            frontmatter = env.page.meta
            
            # Validate frontmatter structure
            validate_archetype_schema(frontmatter)
            
            # Get skill stages from frontmatter
            skill_stages = frontmatter.get('skill_stages', [])
            
            if not skill_stages:
                return "<!-- No skill stages defined in frontmatter -->"
            
            # Generate markdown
            result = []
            for stage in skill_stages:
                stage_name = stage.get('name', 'Unknown Stage')
                topics = stage.get('topics', [])
                
                result.append(f"## {stage_name}")
                result.append("")
                
                if topics:
                    for topic in topics:
                        # Convert topic slug to link
                        topic_link = f"[{topic_slug_to_title(topic)}](../topics/{topic}.md)"
                        result.append(f"* {topic_link}")
                else:
                    result.append("* No topics defined")
                
                result.append("")  # Empty line between stages
            
            return "\n".join(result)
            
        except Exception as e:
            return f"<!-- Error rendering skill stages: {str(e)} -->"
    
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
        
        Returns:
            str: Formatted markdown for cross-references
        """
        try:
            frontmatter = env.page.meta
            
            # Validate frontmatter structure  
            validate_topic_schema(frontmatter)
            
            cross_refs = frontmatter.get('cross_references', [])
            
            if not cross_refs:
                return "<!-- No cross-references defined in frontmatter -->"
            
            result = ["## Related Topics", ""]
            
            for ref in cross_refs:
                title = topic_slug_to_title(ref)
                link = f"[{title}](./{ref}.md)"
                result.append(f"* {link}")
            
            result.append("")
            return "\n".join(result)
            
        except Exception as e:
            return f"<!-- Error rendering cross-references: {str(e)} -->"

    @env.macro
    def render_description() -> str:
        """
        Render the current page description from frontmatter.

        Returns:
            str: Description paragraph or HTML comment if missing.
        """
        try:
            description = env.page.meta.get('description', '').strip()

            if not description:
                return "<!-- No description defined in frontmatter -->"

            return description

        except Exception as e:
            return f"<!-- Error rendering description: {str(e)} -->"


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