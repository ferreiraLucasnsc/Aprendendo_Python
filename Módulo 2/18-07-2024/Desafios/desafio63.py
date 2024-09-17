# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
# de uma Sequência de Fibonacci. 

# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

print('\t\tSEQUENCIADOR FIBONACCI')
numero = int(input('Diga quantos termos de Fibonacci deseja ver: '))
termo1 = 0
termo2 = 1
print(termo1, '-', termo2, end='')
termosMostrados = 3
while termosMostrados <= numero:
    termo3 = termo1 + termo2
    print(' -', termo3, end='')
    termo1 = termo2
    termo2 = termo3
    termosMostrados += 1
print(' -> Fim')