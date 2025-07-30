from itertools import permutations

def caixeiro_viajante(grafo):
    cidades = list(grafo.keys())
    menor_distancia = float('inf')
    melhor_rota = []

    for perm in permutations(cidades):
        distancia_total = 0
        for i in range(len(perm) - 1):
            distancia_total += grafo[perm[i]][perm[i + 1]]
        distancia_total += grafo[perm[-1]][perm[0]]  # Volta ao início

        if distancia_total < menor_distancia:
            menor_distancia = distancia_total
            melhor_rota = perm

    return melhor_rota, menor_distancia

grafo = {}
n = int(input("Digite o número de cidades: "))

for _ in range(n):
    cidade = input("Nome da cidade: ")
    grafo[cidade] = {}

for cidade in grafo:
    for destino in grafo:
        if cidade != destino:
            distancia = int(input(f"Distância de {cidade} para {destino}: "))
            grafo[cidade][destino] = distancia

melhor_rota, menor_distancia = caixeiro_viajante(grafo)
print("Melhor rota:", melhor_rota)
print("Menor distância:", menor_distancia)
