def _validate_grade(subject: str) -> float:
    while True:
        try:
            grade = float(input(f"Enter {subject} grade (0–100): ").strip())
            if 0 <= grade <= 100:
                return grade
            print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def add_students(students: list) -> None:
    try:
        n = int(input("How many students do you want to add?: ").strip())
        if n <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("You must enter an integer.")
        return


    for _ in range(n):
        name = input("Full name: ").strip()
        section = input("Section (e.g., 11B): ").strip()
        spanish  = _validate_grade("Spanish")
        english  = _validate_grade("English")
        social   = _validate_grade("Social Studies")
        science  = _validate_grade("Science")

        avg = (spanish + english + social + science) / 4.0
        student = {
            "name": name,
            "section": section,
            "spanish": spanish,
            "english": english,
            "social": social,
            "science": science,
            "average": avg
        }
        students.append(student)
        print(f"Student '{name}' added successfully.")


def list_students(students: list) -> None:
    if not students:
        print("No students available.")
        return
    print("\nStudents:")
    for s in students:
        print(
            f"{s['name']} ({s['section']}) - "
            f"Avg: {s['average']:.2f} | "
            f"ES:{s['spanish']:.1f} EN:{s['english']:.1f} SO:{s['social']:.1f} SC:{s['science']:.1f}"
        )


def show_top3(students: list) -> None:
    if not students:
        print("No students available.")
        return
    top3 = sorted(students, key=lambda x: x["average"], reverse=True)[:3]
    print("\nTop 3 students:")
    for i, s in enumerate(top3, start=1):
        print(f"{i}. {s['name']} ({s['section']}) - Average: {s['average']:.2f}")


def show_overall_average(students: list) -> None:
    if not students:
        print("No students available.")
        return
    overall = sum(s["average"] for s in students) / len(students)
    print(f"\nOverall average (mean of student averages): {overall:.2f}")
