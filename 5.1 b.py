def last_digit_of_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        c = (a + b) % 10
        a, b = b, c
    
    return b

# Чтение входного значения
n = int(input())
# Вывод последней цифры n-го числа Фибоначчи
print(last_digit_of_fibonacci(n))