#       TIPOS PRIMITIVOS DE DADOS

# Existem diversos tipos de dados, cada um relacionado a um tipo de valor.
# Assim como os dados, as variáveis também possuem tipos específicos de acordo com o dado
# suportado. A distinção entre os tipos de dados é crucial para um programa funcional e
# completo.

# Os tipos de dados mais utilizados são:
# - int: números inteiros (números não decimais)
# - float: números decimais (casas de vírgula e frações)
# - bool: valores booleanos true e false (verdadeiro ou falso)
# - str: strings, ou seja, caracteres juntados em forma de texto

# Para declarar o tipo de dado que será aceito em uma variável, utilizamos o prefixo de
# tipo de dados e incluimos o comando 'input' dentro dos parênteses.

# Exemplo de 'input' com tipo de dado especificado:

numero = int(input('Digite um número: '))
print('O quadrado deste número é', numero * numero)

# Aqui, como foi especificado que a variável seria um número inteiro, conseguimos fazer
# operações matemáticas com a variável, sem ter que especificar seu tipo na linha da
# impressão.

# Uma outra forma de fazer a impressão de uma variável é, adicionado ao comando 'print',
# fazer uso de chaves na área de texto, e usar a sintaxe '.format()' com a variável que
# será impressa.

# Exemplo da nova forma de impressão, usando a variável criada anteriormente:

print('O cubo deste número é {}'.format(numero*numero*numero))

# Aqui, conseguimos imprimir o cubo do número digitado.

# Com a nova sintaxe, podemos usar diversas máscaras que serão substituídas no '.format' com
# os valores especificados.

# Exemplo de mútliplas máscaras impressas:

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
print('A soma entre {} e {} é igual a {}'.format(numero1, numero2, numero1+numero2))

# Aqui, utilizamos as chaves para especificar onde estarão as variáveis. Após isso, usamos
# o '.format' para especificar quais serão as variáveis e sua ordem (sempre da esquerda
# para a direita).
# Caso haja uma necessidade de ordenar de forma diferente, adicione nas aspas a ordem
# dos valores (sempre começando com o número 0 para delimitar o primeiro item).

# Para fins de curiosidade, você pode imprimir um teste lógico utilizando o comando
# 'variavel.is--'. O comando '.is' possui diversas variações que retornam se o que foi
# dito é verdade ou não. Exemplos são se o valor digitado é um número, se é uma letra
# maiúscula, entre outros.

# Exemplo de teste '.is':

valor = input('Digite qualquer coisa: ')
print(valor.isnumeric())

# Aqui, digitamos um valor, e o teste abaixo nos dirá se ele é um número ou não. O resultado
# volta em forma de valor booleano: se é número, True. Se não é, False.