import logic
import finance_manager as fm




def test_create_income_movement_with_positive_amount():
    mov = logic.Logic("Income", "Salary", 1000, "Job").create_movement()
    assert mov == ["Income", "Salary", 1000, "Job"]


def test_create_expense_movement_returns_negative_amount():
    mov = logic.Logic("Expense", "Food", 50, "Groceries").create_movement()
    assert mov == ["Expense", "Food", -50, "Groceries"]


def test_create_expense_movement_if_amount_is_already_negative_it_is_inverted():
    mov = logic.Logic("Expense", "Error", -20, "Other").create_movement()
    assert mov == ["Expense", "Error", 20, "Other"]


def test_create_movement_has_4_fields():
    mov = logic.Logic("Income", "Sale", 10, "Extra").create_movement()
    assert len(mov) == 4


def test_add_category_adds_if_not_exists():
    manager = fm.FinanceManager()
    manager.add_category("Food")
    assert "Food" in manager.categories


def test_add_category_does_not_duplicate():
    manager = fm.FinanceManager()
    manager.add_category("Food")
    manager.add_category("Food")
    assert manager.categories.count("Food") == 1


def test_add_movement_adds_to_list():
    manager = fm.FinanceManager()
    mov = ["Income", "Salary", 1000, "Job"]
    manager.add_movement(mov)
    assert manager.movements == [mov]


def test_finance_manager_starts_with_empty_lists():
    manager = fm.FinanceManager()

    assert manager.categories == []
    assert manager.movements == []
