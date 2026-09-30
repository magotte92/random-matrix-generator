# random-matrix-generator

A random matrix generator for dynamically building maps in Unity.

Requires Python 3.12 or newer. Python 3.12 is the supported baseline. CI also runs the current stable CPython (3.14). There are no runtime dependencies.

## Run

```bash
python new_map.py
```

This writes `mapper.txt` and `setter.txt` in the current working directory.

## Checks

```bash
python -m pip install -r requirements-dev.txt
ruff check .
python -m unittest discover -s tests -v
```
