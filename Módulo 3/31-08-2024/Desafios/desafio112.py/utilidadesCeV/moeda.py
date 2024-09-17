# MÓDULO PARA DESAFIO 111

def aumentar(x, y):
    pct = x * (y / 100)
    res = x + pct
    return res if format is False else moeda(res)

def diminuir(x, y):
    pct = x * (y / 100)
    res = x - pct
    return res if format is False else moeda(res)

def dobro(x):
    res = x * 2
    return res if not format else moeda(res)

def metade(x):
    res =  x / 2
    return res if not format else moeda(res)

def moeda(x, y='R$'):
    return f'{y} {x:.2f}'.replace('.', ',')

def resumoMensagem(x, y):
    print('=' * 30)
    print('RESULTADOS DE ANÁLISES'.center(30))
    print('=' * 30)
    print('Preço analisado:', moeda(x).rjust(30 - 17))
    print('Dobro do preço:', dobro(x).rjust(30 - 16))
    print('Metade do preço:', metade(x).rjust(30 - 17))
    print(f'Aumento de {y}%: {aumentar(x, y).rjust(30 - 16)}')
    print(f'Redução de {y}%: {diminuir(x, y).rjust(30 - 16)}')