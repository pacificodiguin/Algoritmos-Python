import time

def torres_de_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
        return
    else:
        torres_de_hanoi(n - 1, origem, auxiliar, destino)
        print(f"Mover disco {n} de {origem} para {destino}")
        torres_de_hanoi(n - 1, auxiliar, destino, origem)

print("n\tTempo de execução (segundos)")
for n in [21]:
    inicio = time.perf_counter()
    torres_de_hanoi(n, 'A', 'C', 'B')
    fim = time.perf_counter() - inicio
    print(f"{n}\t{fim:.6f}")
    print("-" * 30)