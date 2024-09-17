#       CONDIÇÕES

# A maneira padrão de execução de um programa é seguindo um caminho de fluxo apenas, executando
# cada linha/estrutura passo a passo.
# A adição de condições permite a construção de um código mais complexo, com diferentes caminhos
# de execução para certos casos, mas que chegam no mesmoo resultado (mesmo que este seja o fim
# do programa).

# A estrutura de condições simples utilizada, não apenas em Python, como em outras linguagens, é
# a estrutura 'if-else' (conhecido no Brasil como se-senão);

# Existem dois blocos em uma estrutura if-else: o bloco if, e o bloco else (este é opcional).
# Dada uma condição, o bloco if será executado se a condição for verdadeira (atingida), e o
# bloco else será executado se esta condição for falsa (não for atingida).

# Exemplo de estrutura condicional if-else:

tempoCarro = int(input('Quantos anos tem seu carro? '))
if tempoCarro <= 3:
    print('Seu carro é bem novo.')
else:
    print('Seu carro é bem usado.')

# Aqui, nosso código pode seguir duas direções: se o tempo do carro for menor ou igual a 3, será
# exibida a mensagem no bloco True (if). Senão, será exibida a mensagem no bloco False (else).

# Para reduzir o número de linhas, podemos escrever uma condição simplificada:

idadeUser = int(input('Quantos anos você tem? '))
print('Você é maior de idade.' if idadeUser >= 18 else 'Você é menor de idade.')