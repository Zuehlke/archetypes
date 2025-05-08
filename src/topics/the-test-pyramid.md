# The Test Pyramid

A well-balanced automated testing strategy is often visualised as a pyramid.
At the base are unit tests—small, fast, and reliable tests that verify individual components in isolation.
These should form the majority of your test suite, as they offer quick feedback and are easy to maintain.

In the middle are integration tests, which check that different parts of the system work correctly together.
They're fewer in number and focus on critical interactions.

At the top are end-to-end tests, which simulate real user journeys through the system.
These are the slowest and most fragile, so they should be used sparingly and only for key workflows.

This layered approach helps teams catch bugs early, run tests quickly, and maintain a healthy, sustainable codebase.
The goal isn't just more tests, but the right tests at the right levels.

## Learning Resources

* [Fowler, M. (2014). The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
