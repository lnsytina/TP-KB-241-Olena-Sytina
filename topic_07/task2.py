class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} років"


students = [
    Student("Anna", 20),
    Student("Bohdan", 18),
    Student("Ira", 22),
    Student("Dima", 19)
]

sorted_students = sorted(students, key=lambda s: s.name)

for st in sorted_students:
    print(st)