# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
# à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def leiaInt(txt):
    while True:
        teste = str(input(txt))
        if teste.isnumeric():
            print('Você acabou de digitar o número', teste)
            break
        else:
            print('\033[0;31mERRO! Digite um valor válido.\033[m')
n = leiaInt('Digite um número: ')