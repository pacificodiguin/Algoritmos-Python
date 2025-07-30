def selecionar(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return i
numeros = list(map(int, input("Digite seus numeros separados por espaço: ").split()))
print("Lista ordenada: ", selecionar(numeros))        