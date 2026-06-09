# FunKitPy

> A lightweight Python library and CLI for jokes, dad jokes, roasts, and inspirational quotes.

[![PyPI version](https://img.shields.io/pypi/v/funkitpy.svg)](https://pypi.org/project/funkitpy/)
[![Python versions](https://img.shields.io/pypi/pyversions/funkitpy.svg)](https://pypi.org/project/funkitpy/)
[![License](https://img.shields.io/pypi/l/funkitpy.svg)](LICENSE)

---

## Features

- 🎭 Random jokes
- 👨 Dad jokes
- 🔥 Roasts
- 💬 Inspirational quotes
- 📚 Includes **5,421+ quotes**
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
from funkitpy import joke, dad_joke, roast, quote

print(joke())
print(dad_joke())
print(roast())
print(quote())
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

### Quote

```python
from funkitpy import quote

print(quote())
```

### Quote Data

Returns the raw quote dictionary.

```python
from funkitpy import quote_data

print(quote_data())
```

Example:

```python
{
    "quote": "The best way to get started is to quit talking and begin doing.",
    "author": "Walt Disney"
}
```

---

## Compatibility Aliases

The following aliases are also available:

```python
from funkitpy import (
    get_joke,
    get_dad_joke,
    get_roast,
    get_quote
)
```

These functions behave exactly the same as:

```python
joke()
dad_joke()
roast()
quote()
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

### Quote

```bash
funkit quote
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

Output:

```text
joke
dad-joke
roast
quote
```

---

## Example Output

### Joke

```text
Why don't scientists trust atoms?
Because they make up everything.
```

### Quote

```text
"The best way to get started is to quit talking and begin doing."

— Walt Disney
```

---

## Project Structure

```text
funkitpy/
├── funkitpy/
│   ├── __init__.py
│   ├── jokes.py
│   ├── roasts.py
│   ├── quotes.py
│   ├── cli.py
│   ├── version.py
│   └── data/
│       ├── jokes.json
│       ├── dad_jokes.json
│       ├── roasts.json
│       └── quotes.json
├── tests/
├── pyproject.toml
├── LICENSE
└── README.md
```

---

## Why FunKitPy?

- No API keys required
- No internet connection required
- Lightweight and fast
- Easy Python API
- Simple CLI
- Great for bots, scripts, terminals, and fun projects
- Includes a collection of **5,421+ inspirational quotes**

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
