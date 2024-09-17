# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def analiseMaior(num):
    print('Analisando os valores passados:')
    print('Os números que foram mostrados são:', end=' ')
    cont = 0
    for i in num:
        if cont != len(num) - 1:
            print(i, end=', ')
        else:
            print('e', i)
        cont += 1
    maior = max(num)
    print('Destes', len(num), 'números, o maior foi', maior)
print(f'{' CONTAGEM ':=^50}')
numeros = []
while True:
    num = int(input('Digite um número para a contagem: '))
    numeros.append(num)
    rep = str(input('Deseja adicionar mais algum? [S/N]: '))
    while rep not in 'SsNn':
        rep = str(input('   Tente novamente [S/N]: '))
    if rep in 'Nn':
        break
    print()
print('=' * 50)
analiseMaior(numeros)