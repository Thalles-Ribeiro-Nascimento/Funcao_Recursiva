# 1) Faça uma função recursiva que calcule e retorne o fatorial de um número inteiro N.

def Fatorial(n):
    if n <= 1:
        return 1
    else:
        return n * Fatorial(n - 1)


numb = int(input('Insira um número inteiro: '))
fat = Fatorial(numb)

print(f'O fatorial do número {numb} é igual a {fat}')
