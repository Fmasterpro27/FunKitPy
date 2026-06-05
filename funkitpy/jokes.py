import json
import random
from pathlib import Path

DATA = Path(__file__).parent / "data"

with open(DATA / "jokes.json", encoding="utf-8") as f:
    JOKES = json.load(f)

with open(DATA / "dad_jokes.json", encoding="utf-8") as f:
    DAD_JOKES = json.load(f)

def joke() -> str:
    return random.choice(JOKES)["joke"]

def dad_joke() -> str:
    return random.choice(DAD_JOKES)["joke"]