# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('\t\t\t\tCÁLCULO DE UMA P.A')
termo1 = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
termoGeral = 0
n = 1
print('Aqui estão os 10 primeiros termos da progressão:')
for n in range (1, 10+1):
    termoGeral = termo1 + (n - 1) * razao
    print(termoGeral)