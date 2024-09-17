#       DESAFIO 10

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares
# ela pode comprar.

# Considere: US$1,00 = R$3,27

dinheiroReais = float(input('Quantos reais você tem? R$ '))
dinheiroDolares = float(dinheiroReais / 3.27)
print(f'Com R${dinheiroReais}, você pode comprar US${dinheiroDolares}.')