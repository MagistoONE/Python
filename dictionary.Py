dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

# Создаем множества из ключей и значений
keys_set = set(dct.keys())
values_set = set(dct.values())

# Объединяем множества
union_set = keys_set | values_set  # Используем оператор | для объединения

print("Множество ключей:", keys_set)
print("Множество значений:", values_set)
print("Объединенное множество:", union_set)