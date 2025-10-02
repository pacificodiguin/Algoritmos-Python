import time

#Função para calcular os números divisiveis por 3 até N

def divsiveisTRES(n):
    
    div = []
    
    for i in range (1, n + 1):
        
        if i % 3 == 0:
            div.append(i)
    
    return div
    
# Entrada do valor de N
n = int(input("Digite o valor de n: "))

#Inicio do calculo do tempo de execução
inicio = time.perf_counter()
resultado = divsiveisTRES(n)

#Fim do calculo do tempo de execução
fim = time.perf_counter() - inicio

print("Números divisiveis por três até n", n,": ", resultado)
print("Tempo de execução do programa: ", fim)

