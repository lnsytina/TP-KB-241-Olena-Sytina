from operations import Calculator
from logger import log

class CalculatorUI:

    def __init__(self):
        self.calc = Calculator()

    def get_numbers(self):
        a = float(input("Перше число: "))
        b = float(input("Друге число: "))
        log(f"Введено числа: {a}, {b}")
        return a, b

    def run(self):
        while True:
            op = input("Операція (+, -, *, /) або exit: ")

            if op == "exit":
                print("Вихід...")
                break

            a, b = self.get_numbers()

            if op == "+":
                print(self.calc.add(a, b))
            elif op == "-":
                print(self.calc.sub(a, b))
            elif op == "*":
                print(self.calc.mul(a, b))
            elif op == "/":
                print(self.calc.div(a, b))
            else:
                print("Невідома операція!")
                log(f"Невідома операція: {op}")