# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler
# o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em
# cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos
# durante o campeonato.

jogador = {}
gols = []
jogador['nome'] = str(input('Nome do Jogador: '))
cont = int(input(f'Total de partidas de {jogador['nome']}: '))
for i in range (cont):
    gols.append(int(input(f'\tGols na {i+1}ª partida: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('='*50)
print(jogador)
print('-'*50)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('-'*50)
print(f'O jogador {jogador['nome']} esteve em {cont} partidas: ')
for i, j in enumerate(gols):
    print(f'\tNa {i+1}ª partida, fez {j} gols')
print(f'{jogador['nome']} teve, ao todo, {jogador['total']} gols em sua carreira')