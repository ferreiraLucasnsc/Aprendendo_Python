#       DESAFIO 16

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno
# e tangente desse ângulo.

import math
angulo = (float(input('Digite um ângulo em radiano: ')))
sin = float(math.sin(angulo))
cos = float(math.cos(angulo))
tan = float(math.tan(angulo))
print(f'Seno de {angulo}°: {sin:.4f}\nCosseno de {angulo}°: {cos:.4f}\nTangente de {angulo}°: {tan:.4f}')