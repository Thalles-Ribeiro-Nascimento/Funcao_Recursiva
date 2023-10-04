# 4) Faça uma função recursiva que permita somar os elementos de um vetor de inteiros.


def somarVetor(lista):
    if len(lista) == 1:
        return lista[0]
    return lista[0] + somarVetor(lista[1:])


vet = [1, 2, 3, 4, 5]

print(somarVetor(vet))
