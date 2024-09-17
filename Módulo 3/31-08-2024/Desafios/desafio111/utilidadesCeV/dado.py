def leiaDinheiro(msg):
    validacao = False
    while not validacao:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print('  ERRO:', entrada.upper(), 'é um preço inválido')
        else:
            validacao = True
            return float(entrada)