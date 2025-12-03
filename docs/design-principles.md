# Design Principles

This document outlines the key design principles that guide architectural and implementation decisions for the Zühlke Archetypes project.

## Core Principles

### 1. Simplicity Over Normalization

**Principle**: Choose simple, maintainable solutions over highly normalized data structures when the trade-offs favor simplicity.

**Application**: 
- Learning resources are embedded within topics rather than normalized into separate entities
- Accept some duplication when it provides better context and independence
- Prioritize ease of editing and maintenance over database-style optimization

**Rationale**:
- Content creators (not database administrators) will be editing these files
- Contextual information is often more valuable than avoiding duplication
- Simpler structures reduce cognitive load and barriers to contribution

### 2. Context Over Coupling

**Principle**: Preserve contextual information even when it means duplicating data across multiple locations.

**Application**:
- Same learning resource can appear in multiple topics with different descriptions
- Topic-specific metadata (difficulty, focus areas, time estimates) stays with the topic
- Cross-references use slugs but don't enforce rigid relationships

**Example**:
```yaml
# In clean-code.yaml
learning_resources:
  - title: "Clean Code"
    description: "Focus on chapters 2-4 for naming conventions"

# In refactoring.yaml  
learning_resources:
  - title: "Clean Code"
    description: "Chapters 10-12 cover refactoring techniques"
```

### 3. Independence and Portability

**Principle**: Keep entities as self-contained as possible to enable independent editing and maintenance.

**Application**:
- Topics contain all their learning resources internally
- Minimal hard dependencies between data files
- Each topic file can be understood and edited in isolation

**Benefits**:
- Contributors can work on single topics without understanding the entire system
- Topics can be moved, renamed, or reorganized with minimal impact
- Reduces risk of breaking changes when editing content

### 4. Human-Friendly Tooling

**Principle**: Optimize for human readability and contribution experience over technical efficiency.

**Application**:
- YAML chosen over JSON for better readability and comments
- Slug-based references that are meaningful to humans
- Clear file organization that mirrors the website structure

**Rationale**:
- Community-driven project relies on diverse contributors
- Lower barriers to contribution increase project sustainability
- Readable code review and diff processes improve quality

### 5. Fail-Safe Degradation

**Principle**: Design systems that fail gracefully and provide clear feedback when problems occur.

**Application**:
- Missing topic references result in predictable 404 errors
- 404s serve as a roadmap for content creation priorities
- Validation can catch problems before deployment

**Benefits**:
- Contributors get immediate feedback on missing content
- Project maintains functionality even with incomplete data
- Clear guidance on what content needs to be created

### 6. Evolution-Friendly Architecture

**Principle**: Design for change while maintaining backward compatibility and migration paths.

**Application**:
- Gradual migration from markdown-embedded to structured data
- Optional fields that can be added without breaking existing content
- URL structure preservation during architectural changes

**Implementation**:
- JSON Schema allows for evolution while maintaining validation
- File-based approach enables version control and collaborative editing
- Modular structure supports incremental improvements

## Decision Framework

When making design decisions, consider these questions:

1. **Simplicity**: Does this approach reduce cognitive load for contributors?
2. **Context**: Does this preserve important contextual information?
3. **Independence**: Can components be edited and understood in isolation?
4. **Human-Friendly**: Will this be easy for humans to read, edit, and review?
5. **Fail-Safe**: How does this approach handle missing or incorrect data?
6. **Evolution**: How will this decision impact future changes and improvements?

## Trade-off Acknowledgments

These principles sometimes conflict with traditional software engineering practices:

- **Duplication vs. DRY**: We accept some duplication for better context and independence
- **Normalization vs. Simplicity**: We choose flatter structures over highly normalized ones
- **Performance vs. Readability**: We prioritize human readability over parsing efficiency
- **Coupling vs. Consistency**: We prefer loose coupling even if it allows some inconsistency

These trade-offs are intentional and align with the project's goals as a community-driven, content-focused initiative.