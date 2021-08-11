# Resolução referente 1 - If, Elif, Else

'''
Exercício 02: Fazer um programa que pergunte somente a hora do dia ao usuário.
Baseando-se no horário informado, exibe a saudação apropriada.
exemplo: de 0 às 11 "Bom dia!"; 12 às 17 "Boa tarde!" de 18 às 23 "Boa noite!".
Também tem o problema de a pessoa digitar alguma coisa que não seja um número de 0 a 23.
'''

from util import *

while True:
    h = leiaInt('Digite a hora: [xx:00] ')

    if h > 24:
        print('Por Favor, Digite novamente apenas a Hora. [0 á 23]')
    else:
        break

while True:
    m = leiaInt('Digite os minutos: [00:xx] ')

    if m > 60:
        print('Por Favor, Digite novamente apenas os minutos. [0 á 59]')

    else:
        break

print(f'A hora fornecida é {h:02}:{m:02}')

print(saudacao(h))

# OBS: É interessante criar funções adicionais para se obter um clean code mais interessante. Como por exemplo,
# uma função que receba dois parâmetros sendo, um para a hora e outra para minutos. No caso dessa solução acima.