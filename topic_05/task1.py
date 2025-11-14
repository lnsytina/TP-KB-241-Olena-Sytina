import random

options = ["stone", "scissor", "paper"]

user = input("Введіть stone, scissor або paper: ")

if user not in options:
    print("Невірний ввід!")
else:
    value = random.choice(options)
    print(value)

    if user == value:
        print("Нічия!")
    elif (user == "stone" and value == "scissor") or \
         (user == "scissor" and value == "paper") or \
         (user == "paper" and value == "stone"):
        print("Ви перемогли!")
    else:
        print("Ви програли!")
