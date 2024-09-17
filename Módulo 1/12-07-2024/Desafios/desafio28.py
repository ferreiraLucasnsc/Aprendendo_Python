#       DESAFIO 28

# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
# para viagens mais longas.

print('\t\t\t\tCÁLCULO DE PASSAGEM')
print('-'*100)
distanciaViagem = float(input('Digite a distância de sua viagem (km): '))
valorFixo = float(0)
precoPassagem = float(0)
if distanciaViagem <= 200:
    valorFixo = 0.50
else:
    valorFixo = 0.45
precoPassagem = distanciaViagem * valorFixo
print(f'O preço da passagem será de R$ {precoPassagem}.')
print('-'*100)