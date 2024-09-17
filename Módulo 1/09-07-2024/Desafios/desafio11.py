#       DESAFIO 11

# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e
# a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma
# área de 2m².

larguraParede = float(input('Quanto a parede tem de largura? '))
alturaParede = float(input('Quanto a parede tem de altura? '))
areaParede = float(larguraParede * alturaParede)
litroTinta = float(areaParede / 2)
print(f'Para uma parede de {areaParede}m², você terá que usar {litroTinta}L de tinta.')