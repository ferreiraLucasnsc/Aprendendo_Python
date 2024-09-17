# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se
# encontram no intervalo de 1 até 500.

print('A soma dos múltiplos de 3, ímpares, que existem entre 1 e 500 é igual a: ', end='')
soma = 0
valor = 0
for c in range(1, 500):
    if (c % 2 == 1):
        if (c % 3 == 0):
            soma += c
            valor += 1
print(soma)
print(f'Existem {valor} números ímpares, múltiplos de 3, entre 1 e 500.')