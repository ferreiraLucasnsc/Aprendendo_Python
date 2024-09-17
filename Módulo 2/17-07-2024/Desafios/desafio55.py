# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

pesoMaior = 0
pesoMenor = 0
for c in range (0, 5):
    pesoAtual = float(input(f'Digite o {c + 1}º peso: '))
    if c == 0:
        pesoMaior = pesoAtual
        pesoMenor = pesoAtual
    else:
        if pesoAtual > pesoMaior:
            pesoMaior = pesoAtual
        if pesoAtual < pesoMenor:
            pesoMenor = pesoAtual
print(f'O maior peso foi de {pesoMaior} kg')
print(f'O menor peso foi de {pesoMenor} kg')