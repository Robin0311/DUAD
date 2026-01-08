from typing import List
from models import Category, Movement


class FinanceManager:

    def __init__(self):
        self.categories: List[Category] = []
        self.movements: List[Movement] = []

    def get_category_names(self) -> List[str]:
        return [c.name for c in self.categories]

    def add_category(self, name: str) -> bool:
        name = (name or "").strip()
        if not name:
            return False

        lowered = name.lower()
        if any(c.name.lower() == lowered for c in self.categories):
            return False

        self.categories.append(Category(name))
        return True

    def add_movement(self, movement: Movement) -> None:
        self.movements.append(movement)

    def balance(self) -> float:
        return sum(m.signed_amount() for m in self.movements)
