import time
start_time = time.time()

def cubo(n):
    soma = 0
    i=1
    for i in range(n):
        soma = soma + i * i * i
    print(soma)

n = input("Digite: ")
cubo(int(n))
execution_time = start_time - time.time()