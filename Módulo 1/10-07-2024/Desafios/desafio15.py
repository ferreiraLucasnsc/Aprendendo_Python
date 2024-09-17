#       DESAFIO 15

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt
catetoO = float(input('Digite o comprimento do cateto oposto: '))
catetoA = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = sqrt((catetoO**2) + (catetoA**2))
print(f'A hipotenusa deste triângulo vale {hipotenusa}.')