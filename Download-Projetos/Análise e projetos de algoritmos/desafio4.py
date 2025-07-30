def fibonacci(n):
    if n <= 0:
        return[]
    elif n == 1:
        return[0]
    elif n == 2:
        return[0,1]
    
    fib = [0,1]
    for _ in range(n-2):
        fib.append( fib[-1] + fib[-2] )
    return fib
n = int(input("Digite quantos termos da sequencia de fibonacci deseja ver: "))
print("Sequencia de Fibonacci: ", fibonacci(n))    
