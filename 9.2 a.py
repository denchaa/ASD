# Чтение количества запросов
q = int(input())
# Инициализация пустого множества
numbers = set()

# Список для хранения результатов запросов второго типа
results = []

# Обработка запросов
for _ in range(q):
    query = input().strip().split()
    query_type = int(query[0])
    x = int(query[1])
    
    if query_type == 1:
        # Запрос 1-ого типа: добавляем число x во множество
        numbers.add(x)
    elif query_type == 2:
        # Запрос 2-ого типа: проверяем, содержится ли число x во множестве
        if x in numbers:
            results.append(1)
        else:
            results.append(0)

# Вывод результатов запросов второго типа
print("\n".join(map(str, results)))