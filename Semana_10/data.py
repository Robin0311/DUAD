import csv
import os



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
            writer.writerow({
                "name": s["name"],
                "section": s["section"],
                "spanish": s["spanish"],
                "english": s["english"],
                "social": s["social"],
                "science": s["science"],
                "average": s["average"],
            })
    print(f"Data exported to {file_name}")


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
                row["spanish"] = float(row["spanish"])
                row["english"] = float(row["english"])
                row["social"] = float(row["social"])
                row["science"] = float(row["science"])
                row["average"] = float(row["average"])
            except (KeyError, ValueError):
                print("Skipping a malformed row in CSV.")
                continue
            students.append({
                "name": row.get("name", "").strip(),
                "section": row.get("section", "").strip(),
                "spanish": row["spanish"],
                "english": row["english"],
                "social": row["social"],
                "science": row["science"],
                "average": row["average"],
            })
    print(f"Data imported from {file_name}")
    return students
