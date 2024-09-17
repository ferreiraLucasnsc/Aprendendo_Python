# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os
# valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = list()
pares = list()
impares = list()
continuar = ''
while True:
    n = int(input('Digite o valor a ser adicionado à lista: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    continuar = str(input('Deseja continuar? [S/N]: '))
    if continuar in 'Nn':
        break
print(f'Lista completa: {lista}')
print(f'Valores pares digitados: {pares}')
print(f'Valores ímpares digitados: {impares}')