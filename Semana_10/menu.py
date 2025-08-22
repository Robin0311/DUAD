from actions import (
    add_students,
    list_students,
    show_top3,
    show_overall_average
)
from data import export_csv, import_csv


def show_menu():
    students = []
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Enter student information")
        print("2. View all students")
        print("3. View Top 3 students by average grade")
        print("4. View overall average (average of student averages)")
        print("5. Export data to CSV")
        print("6. Import data from CSV")
        print("0. Exit")

        option = input("Select an option: ").strip()

        if option == "1":
            add_students(students)
        elif option == "2":
            list_students(students)
        elif option == "3":
            show_top3(students)
        elif option == "4":
            show_overall_average(students)
        elif option == "5":
            export_csv(students)
        elif option == "6":
            students = import_csv()
        elif option == "0":
            print("👋 Exiting the program...")
            break
        else:
            print("Invalid option. Please try again.")
