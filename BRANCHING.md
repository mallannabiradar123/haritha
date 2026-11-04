# Branching Strategy

## Main Branch

The main branch contains stable and tested code.

## Feature Branches

Each developer creates a separate feature branch.

- feature/logging
- feature/reporting
- feature/api-tests
- feature/config

## Pull Requests

Developers push their changes and create
pull requests to merge into main.

## Merge Conflict Resolution

When two developers modify the same file,
Git identifies a merge conflict.

The conflict is resolved manually by selecting
the correct code and committing the changes.

## Git Stash

Git stash temporarily stores incomplete changes
without committing them.

## Squash

Squash combines multiple small commits into
one meaningful commit.

## GitHub Actions

GitHub Actions automatically executes Pytest
whenever code is pushed or a pull request
is created.

## Release

The stable project is tagged as v1.0.0.