def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Ділення на нуль!"

s = input("Введіть знак операції: ")

a = float(input("Перше число: "))
b = float(input("Друге число: "))

match s:
    case "+":
        print("Результат:", add(a, b))
    case "-":
        print("Результат:", minus(a, b))
    case "*":
        print("Результат:", mult(a, b))
    case "/":
        print("Результат:", div(a, b))
    case _:
        print("Невірна операція!")