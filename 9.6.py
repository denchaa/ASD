from collections import deque
import sys

input = sys.stdin.read
data = input().splitlines()

q = int(data[0])  # Число запросов
queue = deque()   # Инициализация пустой очереди
results = []      # Список для хранения результатов

for i in range(1, q + 1):
    command = data[i].split()
    
    if command[0] == '1':  # Запрос на добавление элемента
        x = int(command[1])
        queue.append(x)  # Добавляем x в конец очереди
        results.append(queue[0])  # Добавляем в результаты элемент в начале очереди
    elif command[0] == '2':  # Запрос на удаление элемента
        queue.popleft()  # Удаляем первый элемент
        if queue:  # Если очередь не пустая
            results.append(queue[0])  # Добавляем в результаты элемент в начале очереди
        else:
            results.append(-1)  # Если очередь пустая, добавляем -1

# Выводим результаты
print('\n'.join(map(str, results)))