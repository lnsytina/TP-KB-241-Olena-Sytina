import csv
from sys import argv

students = []

def load_from_csv(file_name):
    global students
    with open(file_name, "r", newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        students = [row for row in reader]
    print("Дані завантажено!")

def save_to_csv(file_name):
    with open(file_name, "w", newline='', encoding='utf-8') as file:
        fieldnames = ["name", "phone", "surname", "email"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
    print("Дані збережено в CSV!")

def add_student():
    name = input("Введіть ім'я: ")
    phone = input("Введіть телефон: ")
    surname = input("Введіть прізвище: ")
    email = input("Введіть email: ")
    students.append({"name": name, "phone": phone, "surname": surname, "email": email})
    students.sort(key=lambda x: x["name"])
    print("Студент доданий.")

def delete_student():
    name = input("Введіть ім'я для видалення: ")
    global students
    students = [s for s in students if s["name"] != name]
    print("Студент видалений якщо існував.")

def update_student():
    name = input("Введіть ім'я студента для оновлення: ")
    for s in students:
        if s["name"] == name:
            print(f"Поточні дані: {s}")
            new_phone = input(f"Новий телефон ({s['phone']}): ") or s['phone']
            new_surname = input(f"Нове прізвище ({s['surname']}): ") or s['surname']
            new_email = input(f"Новий email ({s['email']}): ") or s['email']
            s.update({"phone": new_phone, "surname": new_surname, "email": new_email})
            print("Дані оновлено.")
            break
    else:
        print("Студента не знайдено.")

def print_all():
    for s in students:
        print(f"{s['name']:10} {s['phone']:12} {s['surname']:12} {s['email']}")

def main():
    if len(argv) < 2:
        print("Помилка: вкажіть CSV файл як аргумент при запуску.")
        return

    file_name = argv[1]
    load_from_csv(file_name)

    while True:
        action = input("\n[C]–додати | [U]–оновити | [D]–видалити | [P]–показати | [X]–вихід: ").lower()
        if action == "c":
            add_student()
        elif action == "u":
            update_student()
        elif action == "d":
            delete_student()
        elif action == "p":
            print_all()
        elif action == "x":
            save_to_csv(file_name)
            print("Програма завершена.")
            break
        else:
            print("Невідома команда.")


if __name__ == "__main__":
    main()
    