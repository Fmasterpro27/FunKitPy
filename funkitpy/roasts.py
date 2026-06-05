import json
import random
from pathlib import Path

DATA = Path(__file__).parent / "data"


with open(DATA / "roasts.json", encoding="utf-8") as f:
    ROASTS = json.load(f)

def roast() -> str:
    return random.choice(ROASTS)["roast"]

def get_roast():
    return roast()