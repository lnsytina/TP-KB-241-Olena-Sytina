students = [
    {"name": "Bob", "grade": 95},
    {"name": "Anna", "grade": 82},
    {"name": "Mike", "grade": 91},
    {"name": "Diana", "grade": 78}
]

print("Сортування за ім'ям:")
sorted_by_name = sorted(students, key=lambda x: x["name"])
print(sorted_by_name)

print("\nСортування за оцінкою:")
sorted_by_grade = sorted(students, key=lambda x: x["grade"])
print(sorted_by_grade)