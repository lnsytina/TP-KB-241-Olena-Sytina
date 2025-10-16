list = [3, 1, 4]
print("Початковий список:", list)

list.append(5)
print("append(5):", list)

list.extend([7, 9])
print("extend([7, 9]):", list)

list.insert(1, 10)
print("insert(1, 10):", list)

list.remove(4)
print("remove(4):", list)

list.sort()
print("sort():", list)

list.reverse()
print("reverse():", list)

copy_list = list.copy()
print("copy():", copy_list)

list.clear()
print("clear():", list)