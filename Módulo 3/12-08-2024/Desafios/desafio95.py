# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
gols = []
jogadores = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    cont = int(input(f'Total de partidas de {jogador['nome']}: '))
    gols.clear()
    for i in range (cont):
        gols.append(int(input(f'\tGols na {i+1}ª partida: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    resp = str(input('Deseja continuar? [S/N]: ')).upper()
    while resp not in 'SsNn':
        resp = str(input('  Digite uma das alternativas [S/N]: ')).upper()
    if resp in 'Nn':
        print()
        break
    print('-'*50)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*50)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*50)
while True:
    leitura = int(input('Digite o código do jogador para análise (Caso não queira, aperte 999): '))
    if leitura == 999:
        break
    if leitura >= len(jogadores):
        print('Não existe este jogador em nossos dados')
        print()
    else:
        print()
        print(f'\tLEVANTAMENTO DE {jogadores[leitura]['nome']}')
        for i, g in enumerate(jogadores[leitura]['gols']):
            print(f'{i + 1}ª partida: {g} gols')
    print('-'*50)
    print()