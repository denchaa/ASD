def lomuto_partition(arr):
    n = len(arr)
    pivot = arr[0]  # Опорный элемент
    i = 1  # Указатель для элементов меньше или равных опорному

    for j in range(1, n):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]  # Обмен
            i += 1

    arr[0], arr[i - 1] = arr[i - 1], arr[0]  # Поместить опорный элемент на правильное место
    return arr

# Чтение входных данных
n = int(input())
arr = list(map(int, input().split()))

# Выполнение разбиения Ломуто
result = lomuto_partition(arr)

# Вывод результата
print(" ".join(map(str, result)))