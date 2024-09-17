# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número, e direi se ele é primo: '))
divisores = 1
condicaoPrimo = 0
for divisores in range (1, numero+1):
    if numero % divisores == 0:
        condicaoPrimo += 1
if condicaoPrimo == 2:
    print(f'O número {numero} é primo.')
else:
    print(f'O número {numero} não é primo.')