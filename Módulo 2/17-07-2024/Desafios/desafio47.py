# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print('Contagem dos pares de 1 até 50:')
for c in range(1, 50+1):
    if c == 2:
        print(c, end='')
    if (c % 2 == 0) and (c != 2):
        print(' -', c, end='')
print('\nFim da contagem de pares.')