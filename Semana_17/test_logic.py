import finance_manager as fm
from models import Movement


def test_movement_income_signed_amount_positive():
    m = Movement("Income", "Salary", 1000, "Job")
    assert m.signed_amount() == 1000


def test_movement_expense_signed_amount_negative():
    m = Movement("Expense", "Food", 50, "Groceries")
    assert m.signed_amount() == -50


def test_movement_amount_is_stored_positive_even_if_negative_input():
    m = Movement("Expense", "Error", -20, "Other")
    assert m.amount == 20
    assert m.signed_amount() == -20


def test_movement_to_row_has_4_fields():
    m = Movement("Income", "Sale", 10, "Extra")
    assert len(m.to_row()) == 4


def test_add_category_adds_if_not_exists():
    manager = fm.FinanceManager()
    assert manager.add_category("Food") is True
    assert "Food" in manager.get_category_names()


def test_add_category_does_not_duplicate_case_insensitive():
    manager = fm.FinanceManager()
    assert manager.add_category("Food") is True
    assert manager.add_category("food") is False
    assert manager.get_category_names().count("Food") == 1


def test_add_movement_adds_to_list():
    manager = fm.FinanceManager()
    mov = Movement("Income", "Salary", 1000, "Job")
    manager.add_movement(mov)
    assert manager.movements == [mov]


def test_finance_manager_starts_with_empty_lists():
    manager = fm.FinanceManager()
    assert manager.categories == []
    assert manager.movements == []
