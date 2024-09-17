#       DESAFIO 25

# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e 
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
print('\t\t\t\tJOGO DA ADIVINHAÇÃO')
print('Eu irei pensar em um número entre 0 e 5. Tente adivinhar em que número eu pensei...')
print('='*100)
numeroCPU = int(randint(0, 5))
numeroUser = int(input('E aí? Em que número eu penei? : '))
if numeroCPU == numeroUser:
    print(f'Nossa! Realmente pensei no número {numeroCPU}! Parabéns!')
else:
    print(f'Que pena. Eu pensei em {numeroCPU}, e não em {numeroUser}. Tente na próxima...')
print('='*100)