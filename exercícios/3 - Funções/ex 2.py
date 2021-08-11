# Resolução referente 3 - Funções

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre
eles.
"""


def soma(n1=0, n2=0, n3=0):
    soma = n1 + n2 +n3
    return soma


numeros = list()
for numero in range(1, 4):
    n = int(input(f'Digite o {numero}º da soma: '))
    numeros.append(n)

s = soma(numeros[0], numeros[1], numeros[2])
print(f'O Resultado da soma é {s}.')