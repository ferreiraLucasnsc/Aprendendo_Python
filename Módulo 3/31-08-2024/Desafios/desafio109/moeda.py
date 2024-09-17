# MÓDULO PARA DESAFIO 109

def aumentar(x, y, format='False'):
    pct = x * (y / 100)
    res = x + pct
    return res if format is False else moeda(res)

def diminuir(x, y, format='False'):
    pct = x * (y / 100)
    res = x - pct
    return res if format is False else moeda(res)

def dobro(x, format='False'):
    res = x * 2
    return res if not format else moeda(res)

def metade(x, format='False'):
    res =  x / 2
    return res if not format else moeda(res)

def moeda(x, y='R$'):
    return f'{y} {x:.2f}'.replace('.', ',')