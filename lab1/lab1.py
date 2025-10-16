students = [
    {"name": "Bob", "phone": "0631234567", "surname": "Smith", "email": "bobsmith@gmail.com"},
    {"name": "Emma", "phone": "0631234567", "surname": "Jones", "email": "emmajones@gmail.com"},
    {"name": "Jon", "phone": "0631234567", "surname": "Brown", "email": "jonbrown@gmail.com"},
    {"name": "Zak", "phone": "0631234567", "surname": "Williams", "email": "zakwilliams@gmail.com"}
]

def printAllList():
    for elem in students:
        print(f"Student name is {elem['name']}, Phone is {elem['phone']}, Surname is {elem['surname']}, Email is {elem['email']}")
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    surname = input("Please enter student surname: ")
    email = input("Please enter student email: ")
    newItem = {"name": name, "phone": phone, "surname": surname, "email": email}
    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("New element has been added")

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print(f"Delete position {deletePosition}")
        del students[deletePosition]

def updateElement():
    name = input("Please enter the name of the student to update: ")
    found = None

    for student in students:
        if student["name"] == name:
            found = student
            break

    if not found:
        print("Element was not found")
        return

    print("Updating info for {found['name']}")

    new_name = input("New name ({found['name']}): ") or found["name"]
    new_phone = input("New phone ({found['phone']}): ") or found["phone"]
    new_surname = input("New surname ({found['surname']}): ") or found["surname"]
    new_email = input("New email ({found['email']}): ") or found["email"]

    updated_student = {
        "name": new_name,
        "phone": new_phone,
        "surname": new_surname,
        "email": new_email
    }

    students.remove(found)

    insert_pos = 0
    for s in students:
        if new_name > s["name"]:
            insert_pos += 1
        else:
            break
    students.insert(insert_pos, updated_student)

    print("Student info has been updated successfully!")

def main():
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ").lower()

        if choice == "c":
            print("New element will be created:")
            addNewElement()
            printAllList()

        elif choice == "u":
            print("Existing element will be updated")
            updateElement()
            printAllList()

        elif choice == "d":
            print("Element will be deleted")
            deleteElement()

        elif choice == "p":
            print("List will be printed")
            printAllList()

        elif choice == "x":
            print("Exit()")
            break

        else:
            print("Wrong choice")

main()