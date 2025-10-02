import time
inicio = time.perf_counter()
def fibo_iter(n):
    
    if n <= 1:
        return n

    a, b, c = 0, 1, 0
    for i in range(1, n+1):
        a = c + b
        b = c
        c = a
    return a



print (fibo_iter(2000))
fim = time.perf_counter() - inicio
print(fim)
