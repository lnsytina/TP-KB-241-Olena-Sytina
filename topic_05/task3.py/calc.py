from functions import add, minus, mult, div
from operations import get_numbers

while True:
    op = input("Введіть операцію (+, -, *, /) або exit: ")

    if op == "exit":
        print("Програма завершена.")
        break

    if op in ["+", "-", "*", "/"]:
        a, b = get_numbers()

        if op == "+":
            print("Результат:", add(a, b))
        elif op == "-":
            print("Результат:", minus(a, b))
        elif op == "*":
            print("Результат:", mult(a, b))
        elif op == "/":
            print("Результат:", div(a, b))
    else:
        print("Невідома операція!")