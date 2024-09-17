#       DESAFIO 30

# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('\t\t\t\tMAIOR E MENOR')
print('-'*100)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
maior = 0
menor = 0
if n1 > n2 and n1 > n3:
    maior = n1
else:
    if n2 > n1 and n2 > n3:
        maior = n2
    else:
        maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
else:
    if n2 < n1 and n2 < n3:
        menor = n2
    else:
        menor = n3

if maior != menor:
    print(f'O maior número entre os digitados é {maior}, e o menor é {menor}.')
else:
    print(f'Foi digitado apenas um número: {maior}')
print('-'*100)