npx prettier README.md --write
uv run isort . --float-to-top
uv run black .
uv run ruff check . --fix
uv run pytest