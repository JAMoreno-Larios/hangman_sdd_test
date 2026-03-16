# AGENTS.md

## Project overview

Refer to `README.md` found in the project's root directory for the 
project overview.

## Stack
- Use `uv` to manage the virtual environment and dependencies where this project will be developed.
- Use `Python` as programming language.
- Use `NLTK` to generate the word list.
- Use `ruff` for code formatting and linting following `PEP8` practices.
- Use `pytest` for unit testing.

## Development environment requirements
- Use `uv venv` to create a virtual environment before attempting to write any code, activate the virtual environment with `source ./venv/bin/activate`.
- To install any dependencies, use `uv pip install`.

## Testing

- For each new function/method generated, write the corresponding unit tests.
- Store tests in `./tests`.
- Use `pytest` as testing suite.

## Code versioning
- ALWAYS create a new git branch before doing any modifications to the codebase.
- New code must pass all tests before attempting to merge into the `main` branch.
- Name new branches in a descriptive manner, for example, if we are working with word selection the branch should be called `word-selection`.
- When the new code is ready for merging, ask the user to manually review the code before executing `git merge`.
- In case there are conflicts between branches, ask the user to fix them.
