# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
# mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep
def sortear(list):
    print('Sorteando valores da lista:')
    sleep(0.5)
    for i in range (0, 5):
        list.append(randint(1, 10))
    cont = 0
    for n in list:
        if cont != len(list) - 1:
            print(n, end='... ', flush=True)
            sleep(0.5)
        else:
            print(f'e {n}!')
        cont += 1
def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    sleep(0.5)
    print('A soma dos valores pares dos sorteados é igual a', soma)
numeros = []
sortear(numeros)
sleep(0.5)
print('=' * 50)
somaPar(numeros)