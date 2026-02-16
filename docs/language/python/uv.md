# uv

## uv add vs uv pip install

## uv run script.py vs uv run python script.py
`uv run` exectutes the script in the context of the project's virtual environment (--active)
`uv run python script.py` explicitly, and former would automatically detects the Python interpreter from `pyproject.toml` or `.python-version`.
## `uv run`
It selects a Python version based on :
- the  `requires-python` constraint in `pyproject.yaml`
- The avaiable Python versions managed by `uv`
```
uv python list
```

- The *highest* compatible version unless explicitly pinned or specified
```
uv venv --python 3.11 # specified
uv python pin 3.11 # pin version by create .python-version file
```
## system python
`uv` managed python versions are not automatically added to your system's PATH so you can't find it by `which python`;

## Install Dependecy
```
uv pip install . # from pyproject.yaml [dependencies]
uv pip list
```
## [Best Practice](https://docs.astral.sh/uv/pip/environments/#creating-a-virtual-environment)
