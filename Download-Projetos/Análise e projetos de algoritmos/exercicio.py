import time
start_time = time.perf_counter()
def somatorioAoCubo(n):
    soma_parc = 0
    i=1
    for i in range(n):
        soma_parc = soma_parc + i*i*i
    print (soma_parc)
        
    
n = input("Digite: ")

somatorioAoCubo(int(n))

execution_time = time.perf_counter() - start_time
print("segundos", execution_time)