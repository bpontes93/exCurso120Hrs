# Trabalhando com laços e listas.

"""
-> É uma lista de listas de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles podem ser duplicados
Exercício
-> Crie uma função que encontra o primeiro duplicado considerando o segundo
    número como a duplicação. Retorne a duplicação considerada.
        Requisitos:
            A ordem do número duplicado é considerada a partir da segunda
            ocorrência do número, ou seja, o número duplicado em si.
            Exemplo:
                [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
                [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
            Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]
# Criando Função.
def repetidos(amostra):
    test = list()               # Variável usada para testar valores em cada lista dentro da lista.
    contagem_de_amostras = 0    # Indicador de qual sub lista está sendo apresentada.
    for item in amostra:        # Laço que percorre cada sub lista
        test.clear()            # Limpa a variável para ser usada a cada sub lista.
        c = 0                   # Indica ao laço seguinte quando chegar no último elemento da lista.
        for valor in item:                  # Laço para elementos dentro da sub lista.
            if valor in test:               # Testa se o elemento está se repetindo.
                contagem_de_amostras += 1   # acompanha qual é a sub lista.
                print(f'A {contagem_de_amostras}° amostra obteve {valor} como primeira repetição') # saída quando há repetição.
                break   # encerra o processo da lista do laço e passa para a seguinte.
            elif valor not in test:     # testa se é a primeira vez que o elemento aparece.
                test.append(valor)      # adiciona o elemento a variável de teste.
                c += 1                  # acompanha em qual elemento da sub lista está.
                if c == len(item):      # testa se é o ultimo elemento da lista.
                    contagem_de_amostras += 1      # acompanha qual é a sub lista.
                    print(f'A {contagem_de_amostras}° amostra não obteve nenhuma repetição.')   # Saída quando não há repetição.

        print()     # espaço de uma linha a cada sub lista.



# Programa principal.
print(repetidos(lista_de_listas_de_inteiros))
