while True:
    user_input = input("Введите целое число (или 'exit' для выхода): ")
    
    # Проверка на команду выхода
    if user_input.lower() == 'exit':
        print("Программа завершена.")
        break
    
    # Проверка, что ввод - целое число (положительное или отрицательное)
    if user_input.lstrip('-').isdigit():
        num = int(user_input)
        # Убираем минус у отрицательных чисел для подсчета цифр
        num_str = user_input.lstrip('-')
        digit_count = len(num_str)
        print(f"В числе {num} содержится {digit_count} цифр.")
    else:
        print("Ошибка: введите целое число или 'exit'!")