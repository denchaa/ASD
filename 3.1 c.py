import math

def combinations_with_repetition(n, k):
    return math.factorial(n + k - 1) // (math.factorial(k) * math.factorial(n - 1))
    
n,k=map(int,input().split())

result = combinations_with_repetition(n, k)
print(result)