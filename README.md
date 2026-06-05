# FunKitPy

> A lightweight Python library for jokes, dad jokes, and roasts — bring the laughs to your Python projects.

[![PyPI version](https://img.shields.io/pypi/v/funkitpy.svg)](https://pypi.org/project/funkitpy/)
[![Python versions](https://img.shields.io/pypi/pyversions/funkitpy.svg)](https://pypi.org/project/funkitpy/)
[![License](https://img.shields.io/pypi/l/funkitpy.svg)](LICENSE)

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- 🎭 **Random Jokes** — Fetch a random joke from a curated collection
- 👨 **Dad Jokes** — Classic, groan-worthy dad jokes on demand
- 🔥 **Roasts** — Playful roasts for light-hearted banter
- 📦 **Zero dependencies** — Pure Python, no external packages required
- ⚡ **Fast & lightweight** — All data is bundled locally, no network calls needed

---

## Installation

Install FunKitPy from PyPI using pip:

```bash
pip install funkitpy
```

Requires Python 3.8 or higher.

---

## Quick Start

```python
from funkitpy import get_joke, get_dad_joke, get_roast

# Get a random joke
print(get_joke())

# Get a dad joke
print(get_dad_joke())

# Get a roast
print(get_roast())
```

---

## Usage

### Random Jokes

```python
from funkitpy import get_joke

joke = get_joke()
print(joke)
# Output: "Why don't scientists trust atoms? Because they make up everything!"
```

### Dad Jokes

```python
from funkitpy import get_dad_joke

joke = get_dad_joke()
print(joke)
# Output: "I'm reading a book about anti-gravity. It's impossible to put down."
```

### Roasts

```python
from funkitpy import get_roast

roast = get_roast()
print(roast)
# Output: "I'd roast you, but my mom said I'm not allowed to burn trash."
```

---

## API Reference

### `get_joke() -> str`

Returns a random joke from the built-in collection.

```python
from funkitpy import get_joke

joke = get_joke()  # str
```

### `get_dad_joke() -> str`

Returns a random dad joke.

```python
from funkitpy import get_dad_joke

joke = get_dad_joke()  # str
```

### `get_roast() -> str`

Returns a random playful roast.

```python
from funkitpy import get_roast

roast = get_roast()  # str
```

---

## Project Structure

```
funkitpy/
├── funkitpy/
│   ├── __init__.py
│   ├── jokes.py
│   ├── dad_jokes.py
│   ├── roasts.py
│   └── data/
│       ├── jokes.json
│       ├── dad_jokes.json
│       └── roasts.json
├── tests/
│   ├── test_jokes.py
│   └── test_roasts.py
├── pyproject.toml
├── demo.py
├── LICENSE
└── README.md
```

---

## Contributing

Contributions are welcome! Whether it's adding new jokes, fixing bugs, or improving the docs — all help is appreciated.

1. Fork the repository
2. Create a new branch (`git checkout -b feature/add-puns`)
3. Commit your changes (`git commit -m 'Add pun support'`)
4. Push to your branch (`git push origin feature/add-puns`)
5. Open a Pull Request

Please make sure your code passes any existing tests before submitting.

---

## Links

- **Homepage:** [github.com/fmasterpro27/FunKitPy](https://github.com/fmasterpro27/FunKitPy)
- **Issues:** [github.com/fmasterpro27/FunKitPy/issues](https://github.com/fmasterpro27/FunKitPy/issues)
- **PyPI:** [pypi.org/project/funkitpy](https://pypi.org/project/funkitpy/)

---

## License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.