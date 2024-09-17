# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
pares = 0
for c in range(1, 6+1):
    numero = int(input('Digite um valor: '))
    if numero % 2 == 0:
        soma += numero
        pares += 1
if pares > 1:
    print(f'Dentre os seis valores digitados, {pares} deles eram pares.')
    print(f'A soma destes {pares} valores é igual a {soma}')
else:
    print('Dentre os seis valores digitados, nenhum deles eram pares.')