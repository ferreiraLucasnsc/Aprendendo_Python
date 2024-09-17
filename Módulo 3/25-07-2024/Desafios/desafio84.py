# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = list()
insert = list()
maior = menor = 0
while True:
    insert.append(str(input('Nome: ')))
    insert.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = insert[1]
    else:
        if insert[1] > maior:
            maior = insert[1]
        if insert[1] < menor:
            menor = insert[1]
    pessoas.append(insert[:])
    insert.clear()
    continuar = input('Deseja continuar a adição de pessoas? [S/N]: ')
    if continuar in 'Nn':
        break
    print('----------------------------------------------------------')
print(f'Ao todo, foram registradas {len(pessoas)} pessoas')
print(f'O maior peso registrado foi de {maior} kg', end='. Peso de: ')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso registrado foi de {menor} kg', end='. Peso de: ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}')