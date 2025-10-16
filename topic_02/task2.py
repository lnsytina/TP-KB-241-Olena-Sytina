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

print("Оберіть операцію: +, -, *, /")
s = input("Введіть знак операції: ")

a = float(input("Перше число: "))
b = float(input("Друге число: "))

if s == "+":
    print("Результат:", add(a, b))
elif s == "-":
    print("Результат:", minus(a, b))
elif s == "*":
    print("Результат:", mult(a, b))
elif s == "/":
    print("Результат:", div(a, b))
else:
    print("Невірний знак!")