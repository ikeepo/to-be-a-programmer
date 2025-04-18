# uv

## uv add vs uv pip install

## uv run script.py vs uv run python script.py
`uv run` exectutes the script in the context of the project's virtual environment (--active)
`uv run python script.py` explicitly, and former would automatically detects the Python interpreter from `pyproject.toml` or `.python-version`.
