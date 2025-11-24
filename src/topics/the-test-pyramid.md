d---
title: The Test Pyramid
learning_resources:
  - type: "book"
    title: "The Practical Test Pyramid"
    author: "Martin Fowler"
    url: "https://martinfowler.com/articles/practical-test-pyramid.html"
  - type: "course"
    title: "Writing Good Tests with JUnit"
    url: "https://wd3.myworkday.com/zuehlke/learning/course/63dc6ad4fa471000a4cd260b776e0000?type=9882927d138b100019b6a2df1a46018b"
    is_internal: true
---

# The Test Pyramid

A well-balanced automated testing strategy is often visualised as a pyramid. At the base are unit tests—small, fast, and reliable tests that verify individual components in isolation. These should form the majority of your test suite, as they offer quick feedback and are easy to maintain.

In the middle are integration tests, which check that different parts of the system work correctly together. They're fewer in number and focus on critical interactions.

At the top are end-to-end tests, which simulate real user journeys through the system. These are the slowest and most fragile, so they should be used sparingly and only for key workflows.

This layered approach helps teams catch bugs early, run tests quickly, and maintain a healthy, sustainable codebase. The goal isn't just more tests, but the right tests at the right levels.

{{ render_learning_resources() }}
