book = {"1": "Hello", "2": "World"}
print("Cловник:", book)

book.update({"3": "Good"})
print("update({'3': 'Good'}):", book)

print("keys():", book.keys())

print("values():", book.values())

print("items():", book.items())

del book["2"]
print("del 2:", book)

book.clear()
print("clear():", book)