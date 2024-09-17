# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o
# ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto
# NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date
def decisaoVoto(nasc):
    atual = date.today().year
    idade = atual - nasc
    if idade < 16:
        voto = 'NEGADO'
    elif 16 <= idade < 18 or idade >= 65:
        voto = 'OPCIONAL'
    else:
        voto = 'OBRIGATÓRIO'
    print(f'Com {idade} anos, seu voto é: {voto}')

anoNasc = int(input('Digite seu ano de nascimento: '))
decisaoVoto(anoNasc)