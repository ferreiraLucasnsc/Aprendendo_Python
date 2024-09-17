#       CONDIÇÕES ANINHADAS

# As condições vistas até o momento foram condições simples. As estruturas condicionais testavam
# apenas uma condição, no máximo executando dois blocos: a condição sendo verdadeira e a condição
# sendo falsa.
# Programas mais complexos necessitam de levar em consideração - na maioria das vezes - mais de
# uma condição, tomando decisões mais precisas.
# Para estas decisões mais pontuais, utilizamos as estruturas aninhadas.

# Estruturas aninhadas, ou condições aninhadas, são estruturas condicionais que abrigam outras
# estruturas condicionais dentro de si, testando condições dentro de condições.
# Geralmente, as segundas condições se localizam no bloco da condição sendo falsa:

# se (condicao1) {          # Aqui, testamos a primeira condição, retornando um bool
#   ...                     # No caso true, executamos este código
# } senao {                 # No caso false, vamos para a estrutura senao
#   se (condicao2) {        # Aqui, testamos outra condição, sabendo que a primeira é falsa
#       ...                 # No caso true, executamos este código
#   } senao {               # No caso false, vamos para a estrutura senao
#       ...                 # Executamos este código
#   }                       # Fim do segundo senao
# }                         # Fim do primeiro senao

# Antes, tinhamos este fluxo para as condições:

# CONDICAO -> codigo1 -> FIM        # TRUE
#     |                   ^
#     V                   |
# codigo2       ->        o         # FALSE

# Agora, com as condições aninhadas, temos o seguinte fluxo:

# CONDICAO1 -> codigo1 -> FIM       # TRUE para CONDICAO1
#      |                   |
# CONDICAO2 -> codigo2 ->  o        # FALSE para CONDICAO1 e TRUE para CONDICAO2
#      |                   |
# codigo3       ->         o        # FALSE para CONDICAO1 e FALSE para CONDICAO2

# Na linguagem Python, temos três palavras reservadas para as condicionais:
#   IF: criação e teste de condicão                 =   SE
#   ELSE: tratamento do resultado FALSE da condição =   SENAO
#   ELIF: tratamento de FALSE e criação de condição =   SENAO SE

# As condições aninhadas não precisam parar na terceira condição. Podemos fazer diversos aninhamentos
# dependendo da necessidade do programa.