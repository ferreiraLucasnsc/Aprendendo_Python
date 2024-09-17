# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

media = 0
maior = 0
menor = 0
continuar = ''
soma = 0
c = 0
print('\t\tTRATAMENTO DE DADOS')
while continuar != 'N':
    numero = int(input('Digite um valor inteiro: '))
    print('Número computado')
    continuar = str(input('Deseja adicionar outro valor? [S/N] ')).upper()
    soma += numero
    c += 1
    if c == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    if continuar == 'N':
        print('Encerramento das operações:')
media = soma / c
print(f'A média dos {c} números digitados é {media}')
print(f'Dentre esses números, {maior} era o maior e {menor} era o menor')