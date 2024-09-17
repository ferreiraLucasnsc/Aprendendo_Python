# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

from random import randint
print('Pensei em um número entre 0 e 10. Sendo assim, me responda:')
numeroCpu = randint(0, 10)
numero = int(input('Em que número eu pensei? '))
chutes = 0
while numero > 10 or numero < 0:
    print('Este número não está no espaço em que pensei.')
    numero = int(input('Tente novamente: '))
while numero != numeroCpu:
    chutes += 1
    numero = int(input('Tente de novo: '))
print(f'Você acertou! Pensei no número {numeroCpu}!')
if chutes == 0:
    print('Você conseguiu acertar de primeira! Parabéns!!')
else:
    print(f'Foram necessários {chutes} palpites para acertar.')