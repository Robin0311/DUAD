#La herencia multiple permite que una clase herede de mas de una clase base, es util cuando queremos combinar funcionalidades de varias clases


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, i am {self.name} i have {self.age} years old."


# Clase base: Estudiante
class Student:
    def __init__(self, university):
        self.university = university

    def study(self):
        return f"Estudiando en {self.university}."


# Clase base: Empleado
class Employee:
    def __init__(self, company, salary):
        self.company = company
        self.salary = salary

    def work(self):
        return f"Working at {self.company} earning {self.salary} per month."


# Clase que hereda de las tres
class WorkingStudent(Person, Student, Employee):
    def __init__(self, name, age, university, company, salary):
        Person.__init__(self, name, age)
        Student.__init__(self, university)
        Employee.__init__(self, company, salary)

    def full_profile(self):
        return (f"{self.introduce()} "
                f"{self.study()} "
                f"{self.work()}")


work_student = WorkingStudent("Robinson", 32, "Lyfter", "software", 1000)

print(work_student.introduce())     
print(work_student.study())         
print(work_student.work())          
print(work_student.full_profile())
