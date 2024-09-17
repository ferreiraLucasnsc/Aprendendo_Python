# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
jogo1 = dict()
for i in range (1, 5):
    jogo1[i] = randint(1, 6)
print('     JOGO DE DADOS')
print('-'*50)
print(' Valores jogados:')
for j, n in jogo1.items():
    sleep(1)
    print(f'Jogador {j}: número {n}')
sleep(2)
print('='*50)
print('     CLASSIFICAÇÃO DOS JOGADORES')
print()
posicoes = dict(sorted(jogo1.items(), key=lambda item: item[1], reverse=True))
c = 1
for j, n in posicoes.items():
    print(f'{c}º lugar: Jogador {j}, com {n} pontos')
    c += 1