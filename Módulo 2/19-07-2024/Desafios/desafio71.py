# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
# quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('\t\t\t\tCAIXA ELETRÔNICO')
print('=' * 120)

valor = int(input('Qual valor você deseja sacar? R$ '))
while valor < 0:
    valor = int(input('Digite novamente: R$ '))
ced50 = ced20 = ced10 = ced1 = 0
while True:
    if valor >= 50:
        valor -= 50
        ced50 += 1
    elif valor >= 20:
        valor -= 20
        ced20 += 1
    elif valor >= 10:
        valor -= 10
        ced10 += 1
    elif valor >= 1:
        valor -= 1
        ced1 += 1
    if valor == 0:
        break
print('=' * 120)
print('NOTAS A SEREM RECEBIDAS:')
if ced50 > 0:
    print(f'Notas de R$ 50: {ced50}')
if ced20 > 0:
    print(f'Notas de R$ 20: {ced20}')
if ced10 > 0:
    print(f'Notas de R$ 10: {ced10}')
if ced1 > 0:
    print(f'Notas de R$ 1: {ced1}')