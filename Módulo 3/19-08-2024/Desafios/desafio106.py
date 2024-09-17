#  Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# Importante: use cores.

from time import sleep
cores = ('\033[m',  # 0 - sem cor
         '\033[31m', # 1 - vermelho
         '\033[32m', # 2 - verde
         '\033[33m', # 3 - amarelo
         '\033[34m', # 4 - azul
         '\033[35m', # 5 - magenta
         '\033[36m', # 6 - ciano
         )

def ajuda(txt):
    titulo(f'Acessando o manual de \'{txt}\'...', cor=2)
    sleep(1)
    print(cores[5], end='')
    help(txt)
    print(cores[0], end='')

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('-'*tam)
    print(f'  {msg}')
    print('-'*tam)
    print(cores[0], end='')
    sleep(1)

while True:
    titulo('SISTEMA DE AJUDA PyHELP', cor=4)
    digito = str(input('Digite a função/biblioteca (término do programa = FIM): '))
    if digito.upper() == 'FIM':
        print(cores[1])
        print('='*100)
        print(cores[0])
        titulo('FIM DO PROGRAMA', cor=4)
        break
    print(cores[1])
    print('='*100)
    print(cores[0])
    ajuda(digito)
    print(cores[1])
    print('='*100)
    print(cores[0])