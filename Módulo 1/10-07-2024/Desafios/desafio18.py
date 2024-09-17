#       DESAFIO 18

# O mesmo professor do desafio 017 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'A nova ordem de escolhidos é:')
print(f'{lista[0]}\n{lista[1]}\n{lista[2]}\n{lista[3]}')