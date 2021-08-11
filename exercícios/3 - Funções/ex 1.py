# Resolução referente 3 - Funções

"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""
from util import *


def saudacao(nome, sds):
    print('Olá,', end=' ')
    if sds == 'M':
        print('Senhor')

    elif sds == 'F':
        print('Senhora')

    print(f'Seu nome é {nome}')


nome = str(input('Olá, me diga seu nome? ')).capitalize()
sds=' '
while sds not in 'MF':
    sds = str(input('Qual seu sexo:\nM - Masculino\nF - Feminino\nInforme: ')).upper().strip()[0]

linha()
saudacao(nome, sds)