# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = []
for i in range (0, 5):
    n = int(input('Digite um valor a ser adicionado: '))
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na {pos + 1}ª posição da lista...')
                break
            pos += 1
print(f'\nOs valores digitados, em ordem crescente: {lista}')