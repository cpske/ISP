---
title: Process Artifacts Your Project Should Have
---

1. Complete, well-written **iteration plans**.
   * one file per iteration
   * has a "goal" for each iteration
   * has one or more concrete, verifiable milestones in each iteration
   * has list of major work items (broken down into tasks in your task board)

2. Summary of **retrospectives**
   * A retrospective report for each iteration. A separate file in same place as your project docs.
   * Each report contains summary of meeting and concrete process improvement that came out of the meeting, if any
   * If no concrete process improvement in your summary, it means you think your process was fine or perfect

3. **Task board** with...
   * Tasks should be specific and concrete, especially after 1st iteration
   * Has (almost) all tasks for each iteration, including unplanned work
   * Each Task shows the person who did it and time spent

4. **Issues** - work items, requests, and bugs
   * Issues should be specific and clear
   * When closed, should have an explanation of the outcome

5. Github repository with branches, pull requests, pull request comments 

6. CI environment with useful test results
   * You must have good quality, sufficient tests for results to be useful
   * You should merge tests into `master` when you merge the dev branches.

7. **Code coverage reports**, either on Github or in CI

## Software Artifacts Projects Should Have

| What             | Description        |
|------------------|--------------------|
| Cloud Deployment | Runs on cloud      |
| Unit tests       | Good set of tests with at least 80% code coverage, excluding non-logic components like migrations, settings.py, templates |
| E2E Test         | Test many features of deployed app and report any problem |
| Logging          | Log records for activity on the cloud deployment |
| Installation Instructions | How to install and run locally |
| Descriptive README  | Tells others what your project does |

### Desirable but not Required

| What             | Description        |
|------------------|--------------------|
| Development Notes | things you learned that could help another developer |
| Architecture Doc  | notes about the design and technology, rationale for decisions |
