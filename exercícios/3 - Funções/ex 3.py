# Resolução referente 3 - Funções

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""


def aumento(valor, porct):
    return (valor*(porct/100)) + valor


valor = float(input('Digite o preço o produto: R$'))
porct = float(input('Digite a taxa(%) de imposto sobre o valor: '))
vlr_final = aumento(valor, porct)

print(f'O Preço final é R${vlr_final:0.2f}')


