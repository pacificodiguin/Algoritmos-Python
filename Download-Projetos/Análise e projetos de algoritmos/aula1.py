def somar(vetor):
    soma = 0
    for i in vetor:
        soma += i
    print(soma)
    return soma

somar([12,12,4])
# Entrada do usuário
n = int(input("Digite o número de elementos do vetor: "))
if n > 0:
    entrada = input(f"Digite {n} números separados por espaço: ")
    A = list(map(int, entrada.split()))
    if len(A) != n:
        print("Erro: número de elementos não corresponde ao valor de n.")
    else:
        print("Soma dos elementos:", soma_vetor(n, A))
else:
    print("Soma dos elementos: 0")
