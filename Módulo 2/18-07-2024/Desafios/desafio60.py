# Faça um programa que leia um número qualquer e mostre o seu fatorial.

# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input('Digite um número, e calcularei seu fatorial: '))
resultado = 1
print(f'{numero}! = ', end='')
while numero > 0:
    print(numero, end=' ')
    if numero != 1:
        print('x', end=' ')
    else:
        print('=', end=' ')
    resultado *= numero
    numero -= 1
print(resultado)