# traveller-rpg-combat

Combat Encounter Simulations and Balancing for Traveller RPG

This repository uses `uv` for managing Python environments and dependencies. Ensure it is installed.

# Repo Structure

- `notebooks` contain Jupyter notebooks for analysis and exploration and prototypes.
- `src` contains the main codebase.
- `docs` contains documentation and design notes.

# Developers

## Setup

Create and activate the virtual environment:

```bash
uv venv
source .venv/bin/activate
```

Install existing dependencies:

```bash
uv pip install -r requirements.txt
```

## Adding Dependencies

Install a dependency:

```bash
uv pip install <package>
uv pip freeze > requirements.txt
```

## Development - manual tasks

Run tests:

```bash
pytest
```

Check linting:

```bash
ruff check .
```

Format code:

```bash
ruff format .
```

## Pre-commit hooks

This project uses `pre-commit` to run `ruff` checks and formatting before every commit.

```bash
pre-commit install
```

To run manually on all files:

```bash
pre-commit run --all-files
```

Configuration is defined in `.pre-commit-config.yaml`.

## Updating Dependencies

Upgrade packages:

```bash
uv pip install --upgrade <package>
uv pip freeze > requirements.txt
```

## Notes

- Ensure you are using Python 3.12
- Development tools (pytest, ruff) should be listed in `requirements-dev.txt` if separating dev/prod deps
