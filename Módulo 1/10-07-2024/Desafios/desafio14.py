#       DESAFIO 14

# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import floor
numero = float(input('Digite um  número real: '))
print(f'A parte inteira de {numero} é {floor(numero)}.')