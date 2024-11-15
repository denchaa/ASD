def last_digit_of_fibonacci_sum(n):
    # Период Фибоначчи по модулю 10
    pisano_period = 60
    n = n % pisano_period
    
    # Массив для хранения последних цифр Фибоначчи
    fib_last_digits = [0] * (n + 3)
    fib_last_digits[0] = 0
    fib_last_digits[1] = 1
    
    for i in range(2, n + 3):
        fib_last_digits[i] = (fib_last_digits[i - 1] + fib_last_digits[i - 2]) % 10
    
    # Последняя цифра суммы F_0 + F_1 + ... + F_n
    last_digit_sum = (fib_last_digits[n + 2] - 1) % 10
    return last_digit_sum

# Чтение входного значения
n = int(input())
# Вывод последней цифры суммы
print(last_digit_of_fibonacci_sum(n))