# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Alvorecer', 'Travesseiro', 'Girassol', 'Labirinto', 'Esmeralda', 'Bravura',
            'Sinfonia', 'Horizonte', 'Papiro', 'Neblina', 'Euforia', 'Miragem')

print(f'{' LISTA DE PALAVRAS E SUAS VOGAIS ':*^50}')
for p in palavras:
    print(f'Na palavra {p.upper()}, temos as seguintes vogais:', end=' ')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end=' ')
    print('')