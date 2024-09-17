# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = list()
adicionar = 0
continuar = ''
while True:
    adicionar = int(input('Digite o valor a ser adicionado à lista: '))
    if adicionar not in lista:
        lista.append(adicionar)
    else:
        print('Este valor já está na lista...')
    continuar = str(input('Deseja continuar a adição de valores? [S/N]: ')).upper()
    if continuar == 'N':
        print('Terminando adições...')
        break
print()
print('Estes são os valores digitados pelo usuário, em ordem crescente: ')
lista.sort()
print(lista)