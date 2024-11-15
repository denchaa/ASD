from collections import deque

def sum_of_minimums(n, k, a):
    # Дек для хранения индексов
    d = deque()
    sum_min = 0

    for i in range(n):
        # Удаляем индексы, которые выходят за пределы текущего окна
        if d and d[0] < i - k + 1:
            d.popleft()
        
        # Удаляем элементы, которые больше текущего
        while d and a[d[-1]] > a[i]:
            d.pop()
        
        # Добавляем текущий индекс
        d.append(i)
        
        # Если мы достигли размера окна, добавляем минимум в сумму
        if i >= k - 1:
            sum_min += a[d[0]]
    
    return sum_min

# Чтение входных данных
n = int(input())
k = int(input())
a = list(map(int, input().split()))

# Вычисление и вывод результата
result = sum_of_minimums(n, k, a)
print(result)