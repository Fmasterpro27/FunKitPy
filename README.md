# FunKitPy

> A lightweight Python library and CLI for jokes, dad jokes, and roasts.

[![PyPI version](https://img.shields.io/pypi/v/funkitpy.svg)](https://pypi.org/project/funkitpy/)
[![Python versions](https://img.shields.io/pypi/pyversions/funkitpy.svg)](https://pypi.org/project/funkitpy/)
[![License](https://img.shields.io/pypi/l/funkitpy.svg)](LICENSE)

---

## Features

- 🎭 Random jokes
- 👨 Dad jokes
- 🔥 Roasts
- 💻 Command Line Interface (CLI)
- 📦 Zero dependencies
- ⚡ Fast & lightweight
- 🐍 Python 3.8+

---

## Installation

```bash
pip install FunKitPy
```

---

## Quick Start

```python
from funkitpy import joke, dad_joke, roast

print(joke())
print(dad_joke())
print(roast())
```

---

## Python API

### Random Joke

```python
from funkitpy import joke

print(joke())
```

### Dad Joke

```python
from funkitpy import dad_joke

print(dad_joke())
```

### Roast

```python
from funkitpy import roast

print(roast())
```

---

## Compatibility Aliases

The following aliases are also available:

```python
from funkitpy import get_joke
from funkitpy import get_dad_joke
from funkitpy import get_roast
```

These functions behave exactly the same as:

```python
joke()
dad_joke()
roast()
```

---

## Command Line Interface

FunKitPy includes a built-in CLI.

### Random Joke

```bash
funkit joke
```

### Dad Joke

```bash
funkit dad-joke
```

### Roast

```bash
funkit roast
```

### Show Version

```bash
funkit -v
funkit -V
funkit --version
```

### Show Commands

```bash
funkit commands
```

---

## Example Output

```text
Why don't scientists trust atoms?
Because they make up everything.
```

---

## Project Structure

```text
funkitpy/
├── funkitpy/
│   ├── __init__.py
│   ├── jokes.py
│   ├── roasts.py
│   ├── cli.py
│   ├── version.py
│   └── data/
│       ├── jokes.json
│       ├── dad_jokes.json
│       └── roasts.json
├── tests/
├── pyproject.toml
├── LICENSE
└── README.md
```

---

## Contributing

Contributions, bug reports, and feature requests are welcome.

1. Fork the repository
2. Create a branch
3. Make your changes
4. Submit a pull request

---

## Links

Homepage:
https://github.com/fmasterpro27/FunKitPy

Issues:
https://github.com/fmasterpro27/FunKitPy/issues

PyPI:
https://pypi.org/project/funkitpy/

---

## License

Licensed under the Apache License 2.0.
