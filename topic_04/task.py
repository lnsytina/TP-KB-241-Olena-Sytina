def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Помилка: ділення на нуль!"

def get_numbers():
    while True:
        try:
            a = float(input("Перше число: "))
            b = float(input("Друге число: "))
            return a, b
        except ValueError:
            print("Помилка! Потрібно вводити тільки числа. Спробуйте ще раз.\n")

while True:
    s = input("Введіть операцію (+, -, *, /) або 'exit' для виходу: ")

    if s == "exit":
        print("Програма завершена.")
        break

    if s in ["+", "-", "*", "/"]:
        a, b = get_numbers()

        match s:
            case "+":
                print("Результат:", add(a, b))
            case "-":
                print("Результат:", minus(a, b))
            case "*":
                print("Результат:", mult(a, b))
            case "/":
                print("Результат:", div(a, b))
    else:
        print("Невірна операція! Спробуйте ще раз.")