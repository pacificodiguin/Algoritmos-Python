cores = {
      "preto": (0, 1),
    "marrom": (1, 10),
    "vermelho": (2, 100),
    "laranja": (3, 1000),
    "amarelo": (4, 10000),
    "verde": (5, 100000),
    "azul": (6, 1000000),
    "violeta": (7, 10000000),
    "cinza": (8, 100000000),
    "branco": (9, 1000000000),
    "dourado": (-1, 0.1),
    "prateado": (-2, 0.01)
}

tolerancia = {
    "marrom": "±1%",
    "vermelho": "±2%",
    "verde": "±0.5%",
    "azul": "±0.25%",
    "violeta": "±0.1%",
    "cinza": "±0.05%",
    "dourado": "±5%",
    "prateado": "±10%"
}

cor1= input("Digite a 1° cor: ").lower()
cor2 = input("Digite a 2° cor: ").lower()
cor3 = input("Digite a 3° cor (multiplicador): ").lower()
cor4 = input("Digite a 4° cor (tolerância): ").lower()

if cor1 in cores and cor2 in cores and cor3 in cores and cor4 in tolerancia:
    valor = (cores[cor1][0] * 10 + cores[cor2][0]) * cores[cor3][1]
    tol = tolerancia[cor4]
    print(f"Valor do resistor: {valor} Ohn {tol}")
else:
    print("Cor inválida")    