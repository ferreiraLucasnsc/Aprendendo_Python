# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('GERANDO P.A')
termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
n = 1
termoGeral = 1
total = 0
mais = 10
print(f'Estes são os primeiros dez termos da P.A de primeiro termo {termo1} e razão {razao}:')
while mais != 0:
    total += mais
    while n < total+1:
        termoGeral = termo1 + (n - 1) * razao
        print(termoGeral, end=' ')
        if n != 10:
            print(' - ', end='')
        n += 1
    print('PAUSA')
    print('Deseja mostrar quantos termos a mais? (Aperte 0 para encerrar o programa)')
    mais = int(input(': '))
print(f'Fim da progressão aritmética: {total} termos mostrados')