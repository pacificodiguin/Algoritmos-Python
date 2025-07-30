import time

# Função Torres de Hanoi sem Print()
def torres_de_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        return
    else:
        torres_de_hanoi(n - 1, origem, auxiliar, destino)
        torres_de_hanoi(n - 1, auxiliar, destino, origem)

# Entrada dos Valores
valores_n = [3, 6, 9, 12, 15]
print("n (discos)\tTempo de execução (segundos)")
print("-" * 40)

# Tabela do Tempo
for n in valores_n:
    inicio = time.perf_counter()
    torres_de_hanoi(n, 'A', 'C', 'B')
    fim = time.perf_counter() - inicio
    print(f"{n:<10}\t{fim:.6f}")
