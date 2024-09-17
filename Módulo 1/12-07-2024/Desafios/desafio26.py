#       DESAFIO 26

# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

print('\t\t\t\tRADAR ELETRÔNICO')
print('-'*100)
velocidadeCarro = float(input('Digite a velocidade do carro (km/s): '))
multa = 0
if velocidadeCarro > 80.0:
    multa = velocidadeCarro * 7.00
    print('A velocidade do carro é maior que o limite da rodovia.')
    print(f'Aplique uma multa de R$ {multa} ao motorista.')
else:
    print('Tudo certo. Deixe o motorista continuar seu rumo.')
print('-'*100)