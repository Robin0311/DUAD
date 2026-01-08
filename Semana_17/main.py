import FreeSimpleGUI as sg
import interfaces
import finance_manager as fm
import persistence
from models import Movement
from validators import validate_movement_data, ValidationError


# INITIAL CONFIGURATION

headings = ["Type", "Description", "Amount", "Category"]
table_data = []

layout = [
    [sg.Text("Welcome to the Finance Manager")],
    [
        sg.Button("Add Income", key="btnIncome"),
        sg.Button("Add Expense", key="btnExpense"),
        sg.Button("Add Category", key="btnCategory"),
    ],
    [sg.Table(values=table_data, headings=headings, key="globalTable", auto_size_columns=True)],
]

main_window = sg.Window("Finance Manager", layout, finalize=True)

income_window = None
expense_window = None
category_window = None

manager = fm.FinanceManager()

# LOAD DATA

manager.categories, manager.movements = persistence.load()
table_data = [m.to_row() for m in manager.movements]
main_window["globalTable"].update(values=table_data)


# BUTTON STATE

def update_button_state():
    has_categories = len(manager.categories) > 0
    main_window["btnIncome"].update(disabled=not has_categories)
    main_window["btnExpense"].update(disabled=not has_categories)

update_button_state()


while True:
    window, event, values = sg.read_all_windows()

    # MAIN WINDOW
    if window == main_window:

        if event == sg.WIN_CLOSED:
            persistence.save(manager.categories, manager.movements)
            break

        if event == "btnIncome" and income_window is None:
            ui = interfaces.Interfaces("Income")
            income_window = ui.create_window(manager.get_category_names())

        if event == "btnExpense" and expense_window is None:
            ui = interfaces.Interfaces("Expense")
            expense_window = ui.create_window(manager.get_category_names())

        if event == "btnCategory" and category_window is None:
            ui = interfaces.Interfaces("category")
            category_window = ui.create_window(manager.get_category_names())

    # INCOME WINDOW
    elif window == income_window:

        if event == sg.WIN_CLOSED:
            window.close()
            income_window = None

        elif event == "Confirm Income":
            try:
                description, amount, category = validate_movement_data(values)
                movement = Movement("Income", description, amount, category)
            except ValidationError as e:
                sg.popup_error(str(e))
                continue

            manager.add_movement(movement)
            table_data.append(movement.to_row())
            main_window["globalTable"].update(values=table_data)

            persistence.save(manager.categories, manager.movements)
            window.close()
            income_window = None

    # EXPENSE WINDOW
    elif window == expense_window:

        if event == sg.WIN_CLOSED:
            window.close()
            expense_window = None

        elif event == "Confirm Expense":
            try:
                description, amount, category = validate_movement_data(values)
                movement = Movement("Expense", description, amount, category)
            except ValidationError as e:
                sg.popup_error(str(e))
                continue

            manager.add_movement(movement)
            table_data.append(movement.to_row())
            main_window["globalTable"].update(values=table_data)

            persistence.save(manager.categories, manager.movements)
            window.close()
            expense_window = None

    # CATEGORY WINDOW
    elif window == category_window:

        if event == sg.WIN_CLOSED:
            window.close()
            category_window = None

        elif event == "Confirm category":
            name = (values.get("categoryName") or "").strip()
            if not name:
                sg.popup_error("Category name cannot be empty.")
                continue

            added = manager.add_category(name)
            if not added:
                sg.popup_error("That category already exists (or is invalid).")
                continue

            persistence.save(manager.categories, manager.movements)
            update_button_state()

            if income_window:
                income_window["comboCategories"].update(values=manager.get_category_names())
            if expense_window:
                expense_window["comboCategories"].update(values=manager.get_category_names())

            window.close()
            category_window = None

main_window.close()
