def main():
    print("=== Калькулятор степеней ===")
    print("Введите числа или строки, затем степень для возведения\n")
    
    items = []
    
    # Ввод количества элементов с проверкой
    while True:
        try:
            num_items = int(input("Сколько элементов нужно обработать? "))
            if num_items > 0:
                break
            print("🚫 Число должно быть больше 0!")
        except ValueError:
            print("🚫 Ошибка! Введите целое число (например, 3)")

    # Ввод элементов
    for i in range(1, num_items + 1):
        while True:
            item = input(f"Элемент {i}: ")
            if item.replace('.', '', 1).replace('-', '', 1).isdigit():
                items.append(float(item))
                break
            elif item.lstrip('-').replace('.', '', 1).isdigit():
                print("🚫 Некорректное число! Используйте точку для дробей")
            else:
                items.append(item)
                break
    
    # Ввод степени
    while True:
        try:
            power = float(input("\nВведите степень: "))
            break
        except ValueError:
            print("🚫 Ошибка! Введите число (например, 2 или 3.5)")

    # Обработка и вывод
    print("\n🔹 Результаты:")
    for item in items:
        if isinstance(item, (int, float)):
            try:
                result = item ** power
                if isinstance(result, complex):
                    print(f"Комплексное число: ({item})^{power} = {result}")
                else:
                    print(f"Число: {item}^{power} = {result:.4f}" if isinstance(result, float) else f"Число: {item}^{power} = {result}")
            except ZeroDivisionError:
                print(f"⚠️ Ошибка: 0 нельзя возвести в отрицательную степень")
        else:
            try:
                power_int = int(power)
                if power_int >= 0:
                    print(f"Строка: '{item}' × {power_int} = '{item * power_int}'")
                else:
                    print(f"⚠️ Для строк степень должна быть ≥ 0 (вы ввели {power_int})")
            except ValueError:
                print(f"⚠️ Для строк степень должна быть целым числом (вы ввели {power})")

    input("\nНажмите Enter для выхода...")

if __name__ == "__main__":
    main()