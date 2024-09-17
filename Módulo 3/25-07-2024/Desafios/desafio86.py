# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for linha in range (0, 3):
    for coluna in range (0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))
print('===============================================================')
print('\t\tMATRIZ DO USUÁRIO')
for linha in range (0, 3):
    for coluna in range (0, 3):
        print(f'\t\t[{matriz[linha][coluna]:^3}]', end='  ')
    print()