# Resolução referente 4 - Funções, args, kwargs

"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.
"""

def função1():
    try:
        nome = str(input('Digite seu nome: ')).capitalize()
    except (ValueError, TypeError):
        print('Erro, digite novamente.')
    else:
        return nome

def função2(funcao):
    return funcao

print(função2(função1()))


