from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass(frozen=True)
class Category:
    name: str

    def __post_init__(self):
        object.__setattr__(self, "name", (self.name or "").strip())

    def to_dict(self) -> Dict[str, Any]:
        return {"name": self.name}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Category":
        return Category(d.get("name", ""))


@dataclass
class Movement:
    movement_type: str  
    description: str
    amount: float       
    category_name: str

    def __post_init__(self):
        self.movement_type = (self.movement_type or "").strip()
        self.description = (self.description or "").strip()
        self.category_name = (self.category_name or "").strip()
        self.amount = float(self.amount)
        if self.amount < 0:
            self.amount = abs(self.amount)

    def signed_amount(self) -> float:
        return self.amount if self.movement_type == "Income" else -self.amount

    def to_row(self) -> List[Any]:
        return [self.movement_type, self.description, self.signed_amount(), self.category_name]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": self.movement_type,
            "description": self.description,
            "amount": self.amount,
            "category": self.category_name,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Movement":
        return Movement(
            d.get("type", ""),
            d.get("description", ""),
            d.get("amount", 0.0),
            d.get("category", ""),
        )
