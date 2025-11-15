npx prettier README.md --write
uv run isort . --float-to-top
uv run black .
uv run ruff check .
uv run pytest