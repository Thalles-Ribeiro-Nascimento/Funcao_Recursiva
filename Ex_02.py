# 2) Faça uma função recursiva que calcule e retorne o N-ésimo termo da sequência Fibonacci.

def Fibo(n):
    # Caso Base
    if n < 1:
        return 0
    # Caso Recursivo
    if n > 2:
        return Fibo(n - 1) + Fibo(n - 2)
    # Caso Base
    else:
        return 1


f = Fibo(8)
print(f)