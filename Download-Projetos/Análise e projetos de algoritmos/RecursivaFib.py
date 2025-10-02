import time

inicio = time.perf_counter()
def fibo_rec(n):
    if n < 2 :
        return n
    return fibo_rec(n-1) + fibo_rec(n-2)

print (fibo_rec(48))
fim = time.perf_counter() - inicio
print(fim)
