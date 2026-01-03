import FreeSimpleGUI as sg
import interfaces
import logic
import finance_manager as fm
import persistence

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
table_data = list(manager.movements)
main_window["globalTable"].update(values=table_data)

# BUTTON STATE

def update_button_state():
    has_categories = len(manager.categories) > 0
    main_window["btnIncome"].update(disabled=not has_categories)
    main_window["btnExpense"].update(disabled=not has_categories)

update_button_state()

# VALIDATIONS

def validate_movement(values):
    description = (values.get("description") or "").strip()
    amount_text = (values.get("amount") or "").strip()
    category = values.get("comboCategories")

    if not description:
        sg.popup_error("Description cannot be empty.")
        return None

    if not amount_text:
        sg.popup_error("Amount cannot be empty.")
        return None

    try:
        amount = float(amount_text)
    except ValueError:
        sg.popup_error("Amount must be a number.")
        return None

    if not category or category == "Open to see more options":
        sg.popup_error("You must select a category.")
        return None

    return description, amount, category


while True:
    window, event, values = sg.read_all_windows()

    # MAIN WINDOW
    if window == main_window:

        if event == sg.WIN_CLOSED:
            persistence.save(manager.categories, manager.movements)
            break

        if event == "btnIncome" and income_window is None:
            ui = interfaces.Interfaces("Income")
            income_window = ui.create_window(manager.categories)

        if event == "btnExpense" and expense_window is None:
            ui = interfaces.Interfaces("Expense")
            expense_window = ui.create_window(manager.categories)

        if event == "btnCategory" and category_window is None:
            ui = interfaces.Interfaces("category")
            category_window = ui.create_window(manager.categories)

    # INCOME WINDOW
    elif window == income_window:

        if event == sg.WIN_CLOSED:
            window.close()
            income_window = None

        elif event == "Confirm Income":
            data = validate_movement(values)
            if data:
                description, amount, category = data
                income = logic.Logic("Income", description, amount, category)
                movement = income.create_movement()

                manager.add_movement(movement)
                table_data.append(movement)
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
            data = validate_movement(values)
            if data:
                description, amount, category = data
                expense = logic.Logic("Expense", description, amount, category)
                movement = expense.create_movement()

                manager.add_movement(movement)
                table_data.append(movement)
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

            manager.add_category(name)
            persistence.save(manager.categories, manager.movements)

            update_button_state()

            if income_window:
                income_window["comboCategories"].update(values=manager.categories)
            if expense_window:
                expense_window["comboCategories"].update(values=manager.categories)

            window.close()
            category_window = None

main_window.close()
