import requests  

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json")

data = response.json()

rates = {}

for elem in data:
    if elem["cc"] in ["USD", "EUR", "PLN"]:
        rates[elem["cc"]] = elem["rate"]

print("Доступні валюти: USD, EUR, PLN")

currency = input("Введіть тип валюти: ").upper()

if currency not in rates:
    print("Такої валюти немає!")
else:
    amount = float(input("Введіть кількість: "))
    result = amount * rates[currency]
    print("Результат у гривнях:", result)
