# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os
# 10 primeiros termos da progressão usando a estrutura while.

print('GERANDO P.A')
termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
n = 1
termoGeral = 1
print(f'Estes são os primeiros dez termos da P.A de primeiro termo {termo1} e razão {razao}:')
while n < 10+1:
    termoGeral = termo1 + (n - 1) * razao
    print(termoGeral, end=' ')
    if n != 10:
        print(' - ', end='')
    n += 1