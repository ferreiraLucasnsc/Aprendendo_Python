# MÓDULO PARA DESAFIO 108

def aumentar(x):
    pct = x * (10 / 100)
    res = x + pct
    return res

def diminuir(x):
    pct = x * (10 / 100)
    res = x - pct
    return res

def dobro(x):
    return x * 2

def metade(x):
    return x / 2

def moeda(x):
    return f'{x:.2f}'.replace('.', ',')