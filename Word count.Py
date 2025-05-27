def count_words():
    # Ввод строки от пользователя
    text = input("Введите текст: ")
    
    # Разбиваем строку на слова (регистронезависимо)
    words = text.lower().split()
    
    # Создаем словарь для подсчета
    word_count = {}
    
    # Подсчитываем каждое слово
    for word in words:
        # Удаляем знаки препинания вокруг слова
        word = word.strip('.,!?;:"\'()[]')
        if word:  # Проверяем, что слово не пустое после обработки
            word_count[word] = word_count.get(word, 0) + 1
    
    # Выводим результат
    print("\nРезультат подсчета:")
    for word, count in word_count.items():
        print(f"'{word}': {count} раз(а)")

# Запускаем программу
count_words()