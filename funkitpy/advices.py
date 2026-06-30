import json
import random
from pathlib import Path

DATA = Path(__file__).parent / "data"

with open(DATA / "advices.json", encoding="utf-8") as f:
    ADVICES = json.load(f)

def advice() -> str:
    return random.choice(ADVICES)["advice"]

def get_advice():
    return advice()