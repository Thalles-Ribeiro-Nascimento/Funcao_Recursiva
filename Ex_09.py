# 9) Crie uma função recursiva que receba um número inteiro positivo N e calcule o produtório dos números de 1 a N.


def Produto(n):
    if n <= 1:
        return n
    else:
        return n * (Produto(n - 1))


n1 = Produto(3)
print(n1)
