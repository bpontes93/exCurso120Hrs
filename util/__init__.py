'''
3 - Funções criadas para o desenvolvimento de Scripts limpos no decorrer do curso.
'''
from time import sleep


def linha():
    print('=-'*25)


def cabeçalho(msg):
    print('=-'*25)
    print(f'{msg:^50}')
    print('=-'*25)


def leiaInt(msg): #Usual em diversas aplicações
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro! Digite um número inteiro válido!')
            sleep(0.3)
            continue
        else:
            return n


def leiaNome(msg): #Usual em diversas aplicações
    while True:
        try:
            nome = str(input(msg)).capitalize()

        except (ValueError, TypeError):
            print('Erro! Digite caracters válido!')
            sleep(0.3)
            continue

        else:
            return nome








def saudacao(num): #1 - ex.2
    if num <= 11:
        return 'Bom Dia'
    elif num <= 17:
        return 'Boa Tarde'

    elif num <= 23:
        return 'Boa Noite'







