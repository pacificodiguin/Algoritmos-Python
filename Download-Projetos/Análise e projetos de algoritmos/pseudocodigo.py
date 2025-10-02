import time

star_time = time.time()

def processo(i,j,n):

 if i < j:
    i = i + 1
    
 else:
   for k in range(1,n+1):
     i = i * k
 return i
   
i = 2
j = 1
n = 2

resultado = processo(i,j,n)

print(resultado)

print("\n-------------------------------------")

execution_time = time.time() - star_time

print(execution_time)