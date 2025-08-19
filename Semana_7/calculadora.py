Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
def show_menu(current_number):
    print("\n===== CALCULATOR =====")
    print(f"Current number: {current_number}")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Clear result")
    print("0. Exit")


def get_option():
    try:
        return int(input("Select an option: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return None


def get_number():
    try:
        return float(input("Enter the number: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return None


def perform_operation(current_number, option, new_number):
    if option == 1:  
        return current_number + new_number
    elif option == 2:  
        return current_number - new_number
    elif option == 3:  
        return current_number * new_number
    elif option == 4: 
        if new_number == 0:
            print(" Error: Cannot divide by zero.")
            return current_number
        return current_number / new_number
    return current_number


def calculator():
    current_number = 0

    while True:
        show_menu(current_number)
        option = get_option()

        if option is None:
            continue
        if option == 0:
            print("Exiting the calculator...")
            break
        if option < 0 or option > 5:
            print(" Error: Invalid option.")
            continue
        if option == 5:
            current_number = 0
            print(" Result cleared.")
            continue

        new_number = get_number()
        if new_number is None:
            continue

        current_number = perform_operation(current_number, option, new_number)


if __name__ == "__main__":
    calculator()