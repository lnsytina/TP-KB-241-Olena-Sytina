def log(message):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

def add(a, b):
    result = a + b
    log(f"Додавання: {a} + {b} = {result}")
    return result

def sub(a, b):
    result = a - b
    log(f"Віднімання: {a} - {b} = {result}")
    return result

def mul(a, b):
    result = a * b
    log(f"Множення: {a} * {b} = {result}")
    return result

def div(a, b):
    if b == 0:
        log(f"Помилка ділення: {a} / {b} (Помилка: ділення на нуль!)")
        return "Помилка: ділення на нуль!"
    result = a / b
    log(f"Ділення: {a} / {b} = {result}")
    return result