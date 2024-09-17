#       DESAFIO 08

# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

metros = float(input('Digite a distância em metros: '))
cm = float(metros * 100)
mm = float(cm * 10)
print(' '*5, 'CONVERSÃO DE DISTÂNCIAS', ' '*5)
print(f'Metros: {metros}m\nCentímetros: {cm}cm\nMilímetros: {mm}mm')