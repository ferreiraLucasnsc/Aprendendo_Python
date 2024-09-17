#       TRABALHANDO COM MÓDULOS

# O Python, assim como outras linguagens, trabalha com módulos, pacotes instaláveis que permitem
# funcionalidades adicionais. Além dos pacotes adicionais, existem módulos que já vêm instalados
# com a linguagem.

# Módulos possuem grupos de funções distintas, chamados de bibliotecas. A linguagem pode realizar
# importações das bibliotecas para garantir mais funcionalidades em seus programas.
# Para importar bibliotecas para nosso programa, utilizamos o comando 'import' junto ao nome da
# biblioteca, para assim poder trabalhar com as funções adicionais das bibliotecas.
# Usando 'import' biblioteca, importamos todas as funções do grupo. Caso queira algumas seletas,
# usamos a sintaxe: 'from' biblioteca 'import' funcao.

# Uma biblioteca que já vem com a linguagem e está livre para importação é a biblioteca 'math',
# que permite realizar operações matemáticas mais complexas do que os operadores comuns.
# Algumas das funcionalidades adicionais que existem na biblioteca 'math' são: arredondamento
# (ceil/floor), truncação (trunc), potência (pow), raíz quadrada (sqrt), e fatorial (factorial).

# Lembrando da sintaxe de importação:
# import math   ->  importa todas as funções
# from math import factorial    ->  importa apenas a função factorial

# Exemplo de uso da biblioteca 'math':

from math import sqrt, ceil
numero = int(input('Digite um número, e direi sua raíz quadrada: '))
raizNumero = sqrt(numero)
print(f'A raíz quadrada de {numero} é {ceil(raizNumero)}.')

# Aqui, calculamos a raíz e exibimos ela de forma arredondada com as funções da biblioteca.

# Você também pode exibir uma porção seleta de casas decimais:

print(f'A raíz quadrada de {numero} é {raizNumero:.2f}.')

# No site oficial do Python, na aba de documentação, é possível ver as bibliotecas existentes
# e as suas funções para consulta.

# Exemplo de uso de nova biblioteca:

import random
aleatorio = random.randint(1, 10)
print(f'O número aleatório da vez é: {aleatorio}')

# Exemplo de biblioteca externa:

import emoji
print(emoji.emojize('Olha só que legal: :red_heart:'))