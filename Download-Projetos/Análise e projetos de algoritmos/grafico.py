import matplotlib.pyplot as plt
import time
def medir_tempo_execucao(n):   
    inicio = time.time()    
    divisiveisTRES(n)    
    fim = time.time()    
    return fim - inicio
valores_n = list(range(1000, 10001, 1000))
tempos = [medir_tempo_execucao(n) for n in valores_n]
plt.plot(valores_n, tempos, marker='o')
plt.xlabel("n")
plt.ylabel("Tempo de Execução (s)")
plt.title("Desempenho do Algoritmo")
plt.grid(True)
plt.show()