# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
# digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat()
# com a mesma funcionalidade.

def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except(ValueError, TypeError):
            print('  \033[31mERRO: por favor, digite um valor inteiro\033[m')
            continue
        except KeyboardInterrupt:
            print('\n  \033[31mERRO: interrupção pelo usuário\033[m')
            return 0
        else:
            return n

def leiaFloat(txt):
    while True:
        try:
            n = float(input(txt).replace(',','.'))
        except(ValueError, TypeError):
            print('  \033[31mERRO: por favor, digite um valor real\033[m')
            continue
        except KeyboardInterrupt:
            print('\n  \033[31mERRO: interrupção pelo usuário\033[m')
            return 0
        else:
            return n

nInt = leiaInt('Digite um valor inteiro: ')
print(f'O valor digitado foi {nInt}')
print('----------------------------')
nFloat = leiaFloat('Digite um valor real: ')
print(f'O valor digitado foi {nFloat}')