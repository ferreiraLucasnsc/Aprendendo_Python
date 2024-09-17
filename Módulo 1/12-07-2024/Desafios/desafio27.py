#       DESAFIO 27

# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

print('\t\t\t\tANÁLISE NUMÉRICA')
print('.'*100)
numero = int(input('Digite um número: '))
print(f'O número {numero} é par.' if numero % 2 == 0 else f'O número {numero} é ímpar.')
print('.'*100)