# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

print(f'{' LEITURA DE NÚMEROS ':=^120}')
soma = 0
while True:
    numero = int(input('Digite um número, ou digite 999 para parar a leitura: '))
    if numero == 999:
        print('Contagem interrompida')
        break
    soma += numero
print(f'{'---':-^120}')
print(f'A soma entre os números digitados é igual a {soma}')