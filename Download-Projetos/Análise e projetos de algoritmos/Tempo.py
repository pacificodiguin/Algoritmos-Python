import time

#Pode-se usar o perf_counter para tempo menor!

start_time = time.time()

#Cloque o código do seu programa aqui:

def maximo(A):

 max_val = A[0]

 for i in range(1, len(A)):
    if max_val < A[i]:
        max_val = A[i]
 print("máximo: ", max_val)

A = list(input("Digite: "). split())

maximo(A)

execution_time = time.time()-start_time
print("segundos", execution_time)