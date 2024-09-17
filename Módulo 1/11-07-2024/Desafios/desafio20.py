#       DESAFIO 20

#  Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um número: '))
unidade = numero % 10
dezena = (numero % 100) // 10
centena = numero // 100 % 10
milhar = numero // 1000
print(f'Analisando o número {numero}:')
print(f'Unidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}')