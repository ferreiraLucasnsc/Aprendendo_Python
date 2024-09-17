# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

pesoKg = float(input('Digite seu peso (kg): '))
alturaM = float(input('Digite sua altura (m): '))
imc = pesoKg / alturaM**2
statusIMC = str
if imc > 40:
    statusIMC = 'OBESIDADE MÓRBIDA'
elif imc > 30:
    statusIMC = 'OBESIDADE'
elif imc > 25:
    statusIMC = 'SOBREPESO'
elif imc > 18.5:
    statusIMC = 'PESO IDEAL'
else:
    statusIMC = 'ABAIXO DO PESO'
print(f'Baseado em seu IMC ({imc:.2f}kg/m²), seu status é: {statusIMC}')