# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.

def area(lar, alt):
    return lar * alt

print(f'{' CÁLCULO DE TERRENO ':-^50}')
print()
largura = float(input('Digite a largura do terreno, em metros: '))
altura = float(input('Digite a altura do terreno, em metros: '))
are = area(largura, altura)
print(f'A área do terreno {largura} x {altura} é de {are:.2f} m²')