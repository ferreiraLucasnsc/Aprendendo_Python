# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico
# (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    '''
    --> Calcula o fatorial de um número e exibe o processo, caso desejado
    Parâmetros:
        - n: número a ser calculado o fatorial
        - show: decisão de mostrar o processo ou não (opcional)
    '''
    fator = 1
    for i in range(n, 0, -1):
        if show:
            print(i, end=' ')
            if i > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        fator *= i
    if show == False:
        print('O fatorial de', n, 'é igual a', end=' ')
    return fator

numero = int(input('Digite o número para o fatorial: '))
mostrar = str(input('Deseja ver o processo do fatorial? [S/N]: '))
if mostrar in 'Ss':
    mostrarValor = True
else:
    mostrarValor = False
print(fatorial(numero, mostrarValor))