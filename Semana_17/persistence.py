import json
from pathlib import Path

DATA_FILE = Path("finance_manager_data.json")


def save(categories, movements):
    data = {
        "categories": categories,
        "movements": movements
    }

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load():
    if not DATA_FILE.exists():
        return [], []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("categories", []), data.get("movements", [])
    except Exception:
        return [], []
