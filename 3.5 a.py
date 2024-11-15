def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Предполагаем, что минимальный элемент - это текущий элемент
        min_index = i
        for j in range(i + 1, n):
            # Находим индекс минимального элемента
            if arr[j] < arr[min_index]:
                min_index = j
        # Меняем местами найденный минимальный элемент с первым элементом
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Чтение входных данных
n = int(input())
arr = list(map(int, input().split()))

# Сортировка массива
selection_sort(arr)

# Вывод отсортированного массива
print(" ".join(map(str, arr)))