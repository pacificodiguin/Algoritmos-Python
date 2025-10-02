def nPar(n):
  
  for i in n:
    if i%2 == 0:
      print(f"{i} Par")
    else:
      print(f"{i} Impar")
nPar({12,7,8})


def soma_vetor(n, A):
    if n <= 0:
        return 0  
    else:
        return soma_vetor(n - 1, A) + A[n - 1]  


n = int(input("Digite o valor de n (número de elementos a somar): "))

entrada = input("Digite os elementos do vetor separados por espaço: ")
A_completo = list(map(int, entrada.split()))

A = A_completo[:n]

while len(A) < n:
    A.append(0)

resultado = soma_vetor(n, A)
print("Soma dos elementos:", resultado)
