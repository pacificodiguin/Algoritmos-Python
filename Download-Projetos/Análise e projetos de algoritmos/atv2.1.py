import time

def binariorec(n):
    if n > 1:
        binariorec(n // 2)
    print(n % 2, end='')
    
print("n\t Tempo de execução")
for n in [10, 100, 1000, 10000, 100000]:
    inicio = time.perf_counter()
    binariorec(n)
    fim = time.perf_counter() - inicio
    print("|",fim)
