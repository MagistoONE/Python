def find_common_elements():
    # Ввод первого списка чисел
    list1 = input("Введите первый список чисел через пробел: ").split()
    # Ввод второго списка чисел
    list2 = input("Введите второй список чисел через пробел: ").split()
    
    try:
        # Преобразование в множества целых чисел
        set1 = set(map(int, list1))
        set2 = set(map(int, list2))
        
        # Нахождение пересечения множеств
        common_elements = set1.intersection(set2)
        
        if common_elements:
            print("Общие элементы:", sorted(common_elements))
        else:
            print("Нет общих элементов")
    except ValueError:
        print("Ошибка! Вводите только числа, разделенные пробелами")

# Запуск программы
find_common_elements()