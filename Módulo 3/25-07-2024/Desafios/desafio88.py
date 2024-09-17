# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
print('- '*25)
print(f'{'MEGA SENA':^50}')
print(' -'*25)
listaJogo = list()
listaPalpites = list()
jogos = int(input('Quantos jogos deseja gerar? - '))
jogosGerados = 0
while jogosGerados != jogos:
    contNumeros = 0
    while True:
        numero = randint(1, 60)
        if numero not in listaJogo:
            listaJogo.append(numero)
            contNumeros += 1
        if contNumeros >= 6:
            break
    listaJogo.sort()
    listaPalpites.append(listaJogo[:])
    listaJogo.clear()
    jogosGerados += 1
print('='*50)
print(f'{f'{' JOGOS GERADOS ':-^25}':^50}')
for i, l in enumerate(listaPalpites):
    print(f'     JOGO {i + 1}:')
    print(l)
    print('-'*50)