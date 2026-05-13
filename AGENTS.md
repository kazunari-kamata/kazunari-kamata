## Tool execution policy

- This repository uses mise for local development tools.
- Do not assume that tools managed by mise are available directly in PATH.
- Run GitHub CLI commands via `mise exec -- gh`.
- Run Node.js commands via `mise exec -- node` or `mise exec -- npm` when needed.
- Run Python commands via `mise exec -- python` when needed.

## Local path policy

- Do not include absolute local paths in README, documentation, source comments, generated reports, examples, commit messages, pull request titles, or pull request bodies.
- Do not include home directory paths, workspace paths, machine-specific paths, or user-specific paths.
- Use repository-relative paths instead.
- Before creating a commit or pull request, check that generated text does not contain absolute local paths.
