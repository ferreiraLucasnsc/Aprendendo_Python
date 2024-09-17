# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.

from random import randint
print(f'{'   PAR OU ÍMPAR   ':=^120}')
print('Eu escolho um valor de 0 até 10 e você escolhe outro. No final, tente adivinhar se a soma é PAR ou ÍMPAR')
vitoriasUser = 0
escolhaUser = ''
while True:
    valorUser = int(input('Escolha um número: '))
    while True:
        if valorUser < 0 or valorUser > 10:
            valorUser = int(input('Digite um valor de 0 a 10: '))
        else:
            break
    valorCpu = int(randint(0, 10))
    soma = valorUser + valorCpu
    escolhaUser = str(input('Par ou Ímpar? [P/I]: ')).upper()
    while True:
        if escolhaUser != 'P' and escolhaUser != 'I':
            escolhaUser = str(input('Escolha uma das opções [P/I]: ')).upper()
        else:
            break
    print(f'Sua jogada: {valorUser}\nJogada do computador: {valorCpu}\nSoma do total: {soma}')
    if escolhaUser == 'P':
        if soma % 2 == 0:
            print('VOCÊ GANHOU!')
            vitoriasUser += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif escolhaUser == 'I':
        if soma % 2 == 1:
            print('VOCÊ GANHOU!')
            vitoriasUser += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...\n')
print('-'*120)
print(f'Fim de jogo\nTotal de vitórias: {vitoriasUser}')