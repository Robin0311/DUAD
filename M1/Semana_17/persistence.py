import json
from pathlib import Path
from typing import List, Tuple

from models import Category, Movement

DATA_FILE = Path("finance_manager_data.json")


def save(categories: List[Category], movements: List[Movement]) -> None:
    data = {
        "categories": [c.to_dict() for c in categories],
        "movements": [m.to_dict() for m in movements],
    }

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def _load_flexible(data: dict) -> Tuple[List[Category], List[Movement]]:
    raw_categories = data.get("categories", []) or []
    categories: List[Category] = []
    for c in raw_categories:
        if isinstance(c, dict):
            categories.append(Category.from_dict(c))
        elif isinstance(c, str):
            categories.append(Category(c))

    raw_movements = data.get("movements", []) or []
    movements: List[Movement] = []
    for item in raw_movements:
        if isinstance(item, dict):
            movements.append(Movement.from_dict(item))
        elif isinstance(item, list) and len(item) >= 4:
            mtype, desc, amt, cat = item[0], item[1], item[2], item[3]
            movements.append(Movement(str(mtype), str(desc), abs(float(amt)), str(cat)))

    return categories, movements


def load() -> Tuple[List[Category], List[Movement]]:
    if not DATA_FILE.exists():
        return [], []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f) or {}
        return _load_flexible(data)
    except Exception:
        return [], []
