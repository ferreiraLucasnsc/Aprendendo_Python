# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
print('Escolha entre as opções:')
print('[1] Pedra\n[2] Papel\n[3] Tesoura')
escolha = int(input(': '))
escolhaCpu = int(randint(1, 3))
print('Sua escolha:', end=' ')
if escolha == 1:
    print('PEDRA')
elif escolha == 2:
    print('PAPEL')
else:
    print('TESOURA')
print('Minha escolha:', end=' ')
if escolhaCpu == 1:
    print('PEDRA')
elif escolhaCpu == 2:
    print('PAPEL')
else:
    print('TESOURA')
if escolha == escolhaCpu:
    print('Empate!')
elif (escolha == 1 and escolhaCpu == 3) or (escolha == 2 and escolhaCpu == 2) or (escolha == 3 and escolhaCpu == 1):
    print('Você ganhou!')
else:
    print('Eu ganhei!')