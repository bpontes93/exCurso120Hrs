# Exercício de List Comprehension
'''
    Calculando com List Comprehension
'''

carrinho = [('Produto 1', 30), ('Produto 2', 20), ('Produto 3', 50)]

# método 1:
soma_produtos = sum([float(tot[1]) for tot in carrinho])

# método 2:
# soma_produtos = sum(float(y) for x, y in carrinho)


print(soma_produtos)
