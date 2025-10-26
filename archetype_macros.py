"""
Macros for processing archetype and topic frontmatter data.

This module provides MkDocs macros that process YAML frontmatter
to generate structured content for archetypes and topics.
"""

import yaml
import jsonschema
from pathlib import Path
from typing import Dict, List, Any


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
            
            # Validate frontmatter structure (optional for now)
            # validate_archetype_schema(frontmatter)
            
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
    # TODO: Implement JSON schema validation
    # For now, just basic validation
    if 'skill_stages' not in frontmatter:
        raise ValueError("Archetype frontmatter must contain 'skill_stages'")


def validate_topic_schema(frontmatter: Dict[str, Any]) -> None:
    """
    Validate topic frontmatter against JSON schema.
    
    Args:
        frontmatter: The frontmatter data to validate
        
    Raises:
        jsonschema.ValidationError: If frontmatter is invalid
    """
    # TODO: Implement JSON schema validation
    pass