# Чтение количества запросов
q = int(input())

# Инициализация пустого словаря
dictionary = {}

# Список для хранения результатов запросов второго типа
results = []

# Обработка запросов
for _ in range(q):
    query = input().strip().split()
    query_type = int(query[0])
    
    if query_type == 1:
        # Запрос первого типа: "1 x y"
        x = int(query[1])
        y = int(query[2])
        dictionary[x] = y  # Устанавливаем соответствие ключу x числу y
    elif query_type == 2:
        # Запрос второго типа: "2 x"
        x = int(query[1])
        # Проверяем, какое число соответствует ключу x
        # Если ключа нет в словаре, возвращаем -1
        results.append(dictionary.get(x, -1))

# Вывод результатов запросов второго типа
for result in results:
    print(result)