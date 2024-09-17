def leiaDinheiro(msg):
    validacao = False
    while not validacao:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.replace('.', '', 1).isdigit():
            validacao = True
            return float(entrada)
        else:
            print(f'\033[0;31mERRO: "{entrada}" não é um preço válido\033[m')