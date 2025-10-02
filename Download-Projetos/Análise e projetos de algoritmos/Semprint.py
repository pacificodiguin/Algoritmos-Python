import time

def torres_de_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        return
    else:
        torres_de_hanoi(n - 1, origem, auxiliar, destino)
        torres_de_hanoi(n - 1, auxiliar, destino, origem)
        
valores_n = [33,36,39,42]
print("n (discos)\tTempo de execução (segundos)")
print("-" * 40)

for n in valores_n:
    inicio = time.perf_counter()
    torres_de_hanoi(n, 'A', 'C', 'B')
    fim = time.perf_counter() - inicio
    print(f"{n:<10}\t{fim:.6f}")