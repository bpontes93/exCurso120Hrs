# Resolução referente 3 - Funções

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""
from time import sleep


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    return f'{num} não é elegível'




while True:
    try:
        n = int(input('Digite um número: '))
    except (ValueError):
        print('Digite um número inteiro')
    else:
        a = fizzbuzz(n)
        print(a)
        resp = ' '
    while resp not in 'NS':
        resp = str(input('Deseja continuar: [S/N] ')).upper().strip()[0]
    if resp == "N":
        for i in range(0, 3):
            print('.', end=' ')
            sleep(0.3)
        print('FIM')
        break
