import csv
import os


class Student:
    def __init__(self, name, section, spanish, english, social, science):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social = social
        self.science = science
        self.average = (spanish + english + social + science) / 4.0


    def to_dict(self):
        """Convert object to dictionary (for CSV export)."""
        return {
            "name": self.name,
            "section": self.section,
            "spanish": self.spanish,
            "english": self.english,
            "social": self.social,
            "science": self.science,
            "average": self.average,
        }


def student_from_dict(data: dict) -> Student:
    return Student(
        name=data["name"],
        section=data["section"],
        spanish=float(data["spanish"]),
        english=float(data["english"]),
        social=float(data["social"]),
        science=float(data["science"]),
    )


def export_csv(students: list) -> None:
    file_name = "students.csv"
    if not students:
        print("No data to export.")
        return

    fieldnames = ["name", "section", "spanish", "english", "social", "science", "average"]
    with open(file_name, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for s in students:
            writer.writerow(s.to_dict())
    print(f" Data exported to {file_name}")


def import_csv() -> list:
    file_name = "students.csv"
    if not os.path.exists(file_name):
        print("No previously exported CSV file found.")
        return []

    students = []
    with open(file_name, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                student = student_from_dict(row)  # convertimos dict → objeto
                students.append(student)
            except Exception:
                print("Skipping a malformed row in CSV.")
    print(f"Data imported from {file_name}")
    return students
