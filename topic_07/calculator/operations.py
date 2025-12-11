from logger import log

class Calculator:

    def add(self, a, b):
        result = a + b
        log(f"Додавання: {a} + {b} = {result}")
        return result

    def sub(self, a, b):
        result = a - b
        log(f"Віднімання: {a} - {b} = {result}")
        return result

    def mul(self, a, b):
        result = a * b
        log(f"Множення: {a} * {b} = {result}")
        return result

    def div(self, a, b):
        if b == 0:
            log(f"Помилка: ділення {a}/{b}")
            return "Помилка: ділення на нуль!"
        result = a / b
        log(f"Ділення: {a} / {b} = {result}")
        return result