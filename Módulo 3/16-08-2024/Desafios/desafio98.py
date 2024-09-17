# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep
def contagem(i, f, p):
    print(f'Contagem de {i} para {f}, com passo de {p}:')
    sleep(1)
    cont = i
    if i < f:
        while cont <= f:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('// Fim da contagem')
    elif i > f:
        while cont >= f:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('// Fim da contagem')

def linhas():
    print('-' * 50)

contagem(1, 10, 1)
sleep(0.25)
linhas()
contagem(10, 0, 2)
sleep(0.25)
linhas()
print('Agora que você viu que está funcionando a contagem, faça uma só sua!')
inicio = int(input('De onde deseja começar? - '))
fim = int(input('Até aonde deseja contar? - '))
passo = int(input('Qual deve ser o número do passo? - '))
linhas()
contagem(inicio, fim, passo)