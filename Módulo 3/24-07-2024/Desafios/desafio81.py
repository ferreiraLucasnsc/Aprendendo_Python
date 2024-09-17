# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = list()
continuar = ''
while True:
    n = int(input('Digite um valor para ser adicionado à lista: '))
    lista.append(n)
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    if continuar == 'N':
        print('Terminando adições...')
        break
print(f'{' LISTA DO USUÁRIO ':-^50}')
print(f' * Números de elementos adicionados: {len(lista)}')
lista.sort(reverse=True)
print(f' * Lista dos elementos em ordem decrescente: {lista}')
if 5 in lista:
    print(f' * O número 5 está na lista, e está na {lista.index(5) + 1}ª posição')
else:
    print(' * O número 5 não está nesta lista')