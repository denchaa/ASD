def fibonacci_mod(n, mod):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, (a + b) % mod
    return b

def last_digit_of_fibonacci_sum(m, n):
    # Период Фибоначчи по модулю 10
    period = 60
    
    # Приводим m и n к периоду
    m_mod = m % period
    n_mod = n % period
    
    # Считаем F_{n+2} и F_{m+1}
    F_n_plus_2 = fibonacci_mod(n_mod + 2, 10)
    F_m_plus_1 = fibonacci_mod(m_mod + 1, 10)
    
    # Считаем сумму
    last_digit_sum = (F_n_plus_2 - F_m_plus_1) % 10
    
    return last_digit_sum

# Пример использования
m, n = map(int, input().split())
print(last_digit_of_fibonacci_sum(m, n))