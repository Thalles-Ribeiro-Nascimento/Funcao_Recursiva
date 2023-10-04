# 6) Crie um programa em python, que contenha uma função recursiva que receba dois inteiros positivos k e
# n e calcule k^n. Utilize apenas multiplicações.
# O programa principal deve solicitar ao usuário os valores de k e n e imprimir o resultado da chamada da função.


def Potencia(k, n):
    if n == 0:
        return 1

    return k * Potencia(k, n - 1)


print(Potencia(8, 2))
