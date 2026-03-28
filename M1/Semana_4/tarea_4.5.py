# 5.Dada n cantidad de notas de un estudiante, calcular:
# 1. Cuantas notas tiene aprobadas (mayor a 70).
# 2. Cuantas notas tiene desaprobadas (menor a 70).
# 3. El promedio de todas.
# 4. El promedio de las aprobadas.
# 5. El promedio de las desaprobadas.

# Variables
total_grades = 0
grade_counter = 1
current_grade = 0
passed_grades_count = 0
failed_grades_count = 0
average_passed_grades = 0
average_failed_grades = 0
overall_average = 0

print("Enter the total number of grades:")

total_grades = int(input())

while grade_counter <= total_grades:
    print("Enter grade number")
    print(grade_counter)
    
    current_grade = float(input())

    if current_grade < 70:
        failed_grades_count += 1
        average_failed_grades += current_grade
    else:
        passed_grades_count += 1
        average_passed_grades += current_grade

    overall_average += (current_grade / total_grades)

    grade_counter += 1

# Calculate average of failed grades (if any)
if failed_grades_count > 0:
    average_failed_grades = average_failed_grades / failed_grades_count
else:
    average_failed_grades = 0

# Calculate average of passed grades (if any)
if passed_grades_count > 0:
    average_passed_grades = average_passed_grades / passed_grades_count
else:
    average_passed_grades = 0

# Display results
print("The student has this number of passing grades:")
print(passed_grades_count)

print("This is the average of the passing grades:")
print(f"{average_passed_grades:.2f}")

print("The student has this number of failing grades:")
print(failed_grades_count)

print("This is the average of the failing grades:")
print(f"{average_failed_grades:.2f}")

print("This is the overall average grade:")
print(f"{overall_average:.2f}")
