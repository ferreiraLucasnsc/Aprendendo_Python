# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a
# ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(j='<desconhecido>', g=0):
    print(f'O jogador {j} fez {g} gol(s) em campo')

jogador = str(input('Digite o nome do jogador: '))
gols = str(input(f'Digite a quantidade de gols do jogador: '))
print('-' * 10)
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    ficha(g = gols)
else:
    ficha(jogador, gols)