def find_insert_position(list, value):
    for i in range(len(list)):
        if value < list[i]:
            return i
    return len(list)

sorted_list = [1, 3, 5, 7, 9]
print("Відсортований список:", sorted_list)

new_value = int(input("Введіть число для вставки: "))

position = find_insert_position(sorted_list, new_value)
print("Позиція для вставки:", position)

sorted_list.insert(position, new_value)
print("Новий список:", sorted_list)