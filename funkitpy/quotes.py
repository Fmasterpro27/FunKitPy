import json
import random
from pathlib import Path

DATA = Path(__file__).parent / "data"

with open(DATA / "quotes.json", encoding="utf-8") as f:
    QUOTES = json.load(f)

def quote() -> str:
    q = random.choice(QUOTES)
    return f'"{q["quote"]}"\n\n— {q["author"]}'

def quote_data() -> dict:
    return random.choice(QUOTES)