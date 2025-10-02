import time
import os

def print_tabuleiro(tabuleiro):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
    for linha in tabuleiro:
        print(" ".join(f"{cel:2}" if cel > 0 else "__" for cel in linha))
    print()
    time.sleep(0.1)  # Pausa entre passos (ajustável)

def passeio_do_cavalo(n, x_inicio, y_inicio):
    tabuleiro = [[0 for _ in range(n)] for _ in range(n)]
    
    movimentos = [
        (-2, -1), (-2, +1),
        (-1, -2), (-1, +2),
        (+1, -2), (+1, +2),
        (+2, -1), (+2, +1),
    ]
    
    def pode_mover(x, y):
        return 0 <= x < n and 0 <= y < n and tabuleiro[x][y] == 0

    def resolver(x, y, passo):
        tabuleiro[x][y] = passo
        print_tabuleiro(tabuleiro)

        if passo == n * n:
            return True

        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy
            if pode_mover(nx, ny):
                if resolver(nx, ny, passo + 1):
                    return True

        tabuleiro[x][y] = 0  # backtracking
        print_tabuleiro(tabuleiro)
        return False

    # ⏱️ Marca o tempo de início
    inicio = time.time()

    if resolver(x_inicio, y_inicio, 1):
        fim = time.time()
        print(f"✅ Solução encontrada em {fim - inicio:.4f} segundos.")
    else:
        fim = time.time()
        print("❌ Nenhuma solução encontrada.")
        print(f"⏱️ Tempo total: {fim - inicio:.4f} segundos.")

# Exemplo: tabuleiro 5x5, começando da posição (2, 2)
passeio_do_cavalo(5, 0, 0)


