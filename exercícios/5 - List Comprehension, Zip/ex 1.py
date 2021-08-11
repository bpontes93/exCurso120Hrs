# Exercício de List Comprehension
'''
    Desafio - Manipular o valor de string  separando tendo resultado um conjunto
    de 0 a 9 e depois adicionar um ponto entre cada grupo.
'''
string = '01234567890123456789012345678901234567890123456789012345678901234567890123456789'

lista_separado = [string[i:i + 10] for i in range(0, len(string), 10)]

ponto_separa = '.'. join(lista_separado)

print(lista_separado)
print(ponto_separa)

