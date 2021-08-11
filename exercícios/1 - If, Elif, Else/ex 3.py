# Resolução referente 1 - If, Elif, Else

'''
Exercício 03: Faça um programa que peça o primeiro nome do usuário.
Se o nome tiver quatro letras ou menos, escreva "seu nome é curto".
Se tiver entre cinco e seis letras, escreva "seu nome é normal".
Se tiver mais de seis letras, escreva "seu nome é muito grande".
'''
from util import *
cabeçalho('Descubra a extensão de seu nome.')
while True:
    nome = leiaNome('Digite seu nome: ')
    if nome.isnumeric():
        print('Erro, não é possivel ter números em seu nome. Tente novamente.')
    else:

        print(f'Prazer, {nome}')
        if len(nome) < 4:
            print('Seu nome possui tamanho curto.', end=' ')
        elif len(nome) < 6:
            print('Seu nome possui tamanho normal.', end=' ')
        elif len(nome) > 6:
            print('Seu nome possui tamanho grande.', end=' ')
        print(f'Contém {len(nome)} letras.')
        linha()

        break


