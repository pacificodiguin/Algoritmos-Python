import time

inicial = time.perf_counter()

def iterativo(n, A):
    maior = A[0]
    for i in range(1, n):
        if A[i] > maior:
            maior = A[i]
    return maior
final = inicial - time.perf_counter()

inicio = time.perf_counter()

def recursivo(n, A):
    
    if n == 1:
        return A[0] 
    else:
        max_restante = recursivo(n - 1, A)
        return max_restante if max_restante > A[n - 1] else A[n - 1]
    
fim = inicio - time.perf_counter()

n = int(input("Digite um número n: "))

if n < 1:
    print("Valor inválido. n deve ser maior ou igual a 1.")
else:
    A = list(range(1, n + 1))  

    print("Vetor A:", A)
    
    max_iter = iterativo(n,A)
    print("Maior elemento (iterativo):", max_iter)

    max_rec = recursivo(n, A)
    print("Maior elemento (recursivo):", max_rec)
    
print("Calculo comp(iterativo):",final)    
    
print("Calculo comp(recursivo):",fim)
