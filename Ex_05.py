# 5) Crie uma função recursiva que receba um número inteiro positivo N
# e calcule o somatório dos números de 1 a N.

def Soma(n):

    # Caso Base
    if n == 0:
        return 0

    # Caso Recursivo
    return n + Soma(n - 1)



numb = int(input('Insira um valor: '))
s = Soma(numb)

print(f'Soma de todos os valores de 1 a {numb} = {s}')
