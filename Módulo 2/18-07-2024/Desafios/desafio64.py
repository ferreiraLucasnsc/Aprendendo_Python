# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
# usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag).

print('\t\tSOMA DE NÚMEROS')
print('(Para parar o programa, aperte o número 999)')
numero = 0
soma = 0
digitados = 0
while numero != 999:
    numero = int(input('Digite um número inteiro: '))
    if numero != 999:
        soma += numero
        digitados += 1
print(f'A soma dos {digitados} números digitados é igual a {soma}')