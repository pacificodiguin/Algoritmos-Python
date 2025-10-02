import time
inicio = time.perf_counter()

def somar(n, A):
    if n <= 0:
        return 0  
    else:
        return somar(n - 1, A) + A[n - 1] 

fim = inicio - time.perf_counter()

n = int(input("Digite um número n: "))

A = list(range(1, n + 1))

resultado = somar(n, A)

print("Vetor A:", A)
print("Soma dos elementos de A[1...",n,"] é: ",resultado)


print("Calculo computacional: ",fim)


        