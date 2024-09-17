# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

listaUser = list()
posicaoMaior = 0
posicaoMenor = 0
for i in range(0, 5):
    item = int(input(f'Digite o {i + 1}º valor: '))
    listaUser.append(item)
print(f'A sua lista criada foi: {listaUser}')
for i, valor in enumerate(listaUser):
    if valor == max(listaUser):
        posicaoMaior = i
    if valor == min(listaUser):
        posicaoMenor = i
print(f'Destes valores, o maior foi {max(listaUser)}, localizado na {posicaoMaior + 1}ª posição')
print(f'Destes valores, o menor foi {min(listaUser)}, localizado na {posicaoMenor + 1}ª posição')