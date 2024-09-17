# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que
# estão na tupla.

from random import randint
numeros = tuple(randint(1, 10) for i in range(5))
print('Sorteei os seguintes números:', numeros)
numerosOrdem = sorted(numeros)
print('Destes números, o maior é', numerosOrdem[-1], 'e o menor é', numerosOrdem[0])

'''print(f'O maior valor é", max(numeros))'''
'''print(f'O menor valor é", min(numeros))'''