import time

def binariorec(n):
    if n > 1:
        binariorec(n // 2)
    print(n % 2, end='')

numero = 12
print(f"Representação binária de {numero}:", end=" ")
inicio = time.perf_counter()
binariorec(numero)
print()
fim = time.perf_counter() - inicio
print("Tempo de Execução: ",fim)