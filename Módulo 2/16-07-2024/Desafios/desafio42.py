# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

lado1 = float(input('Digite a medida do primeiro lado: '))
lado2 = float(input('Digite a medida do segundo lado: '))
lado3 = float(input('Digite a medida do terceiro lado: '))
if lado1 < lado2 + lado3 and lado2 < lado3 + lado1 and lado3 < lado1 + lado2:
    print('Estes três lados podem formar um triângulo ', end='')
    if lado1 != lado2 and lado2 != lado3:
        print('ESCALENO.')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print('ISÓSCELES.')
    else:
        print('EQUILÁTERO.')
else:
    print('Estes três lados não podem formar um triângulo.')