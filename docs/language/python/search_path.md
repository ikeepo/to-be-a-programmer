# Search Path
The directory of the script being run (or the current directory for interactive sessions).

Directories listed in the PYTHONPATH environment variable.

Python’s standard library directories.

Directories for installed third-party packages (e.g., in your Poetry virtual environment).

Any additional paths added by tools like Poetry or pytest.

# How to import module source from test
```shell
PYTHONPATH=$PWD pytest test/
```
