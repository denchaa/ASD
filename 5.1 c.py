def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        # Период начинается с 0, 1
        if previous == 0 and current == 1:
            return i + 1

def fibonacci_mod(n, m):
    # Находим период Пизано
    period = pisano_period(m)
    n = n % period  # Сокращаем n по модулю периода
    previous, current = 0, 1
    if n == 0:
        return previous
    elif n == 1:
        return current
    else:
        for _ in range(n - 1):
            previous, current = current, (previous + current) % m
        return current

# Чтение входных данных
n, m = map(int, input().split())
# Вычисление и вывод результата
print(fibonacci_mod(n, m))