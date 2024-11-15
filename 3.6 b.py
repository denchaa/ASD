def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Чтение входных данных
n = int(input())
arr = list(map(int, input().split()))

# Сортировка массива
sorted_arr = quicksort(arr)

# Вывод отсортированного массива
print(" ".join(map(str, sorted_arr)))