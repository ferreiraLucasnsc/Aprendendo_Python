# Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
somaTotal = 0
somaTerc = 0
valoresSeg = []
for linha in range (0, 3):
    for coluna in range (0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            somaTotal += matriz[linha][coluna]
        if coluna == 2:
            somaTerc += matriz[linha][2]
        if linha == 1:
            valoresSeg.append(matriz[1][coluna])
print('===============================================================')
print('\t\t    MATRIZ DO USUÁRIO')
for linha in range (0, 3):
    print('', end='\t\t')
    for coluna in range (0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print()
print()
print(f'A soma de todos os valores pares da matriz é: {somaTotal}')
print(f'A soma dos valores da terceira coluna é: {somaTerc}')
print(f'Dos valores da segunda linha, o maior é: {max(valoresSeg)}')