# Запрос данных у пользователя
name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
age = input("Введите ваш возраст: ")

# Вывод с использованием метода format()
print("Ваше имя: {}, Фамилия: {}, Возраст: {} лет.".format(name, surname, age))

# Вывод с использованием f-строки
print(f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет.")