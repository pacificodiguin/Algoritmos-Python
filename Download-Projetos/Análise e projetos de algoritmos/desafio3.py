def polindromo(palavra):
    return palavra == palavra[::-1]
palavra = input("Digite uma palavra: ").lower()
print(f"a palavra '{palavra}' é um polindromo?", polindromo(palavra))
