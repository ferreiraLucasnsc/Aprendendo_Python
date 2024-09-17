#       OPERADORES MATEMÁTICOS

# Assim como outras linguagens, o Python é capaz de realizar operações matemáticas, através dos
# operadores, símbolos especiais que denotam funções distintas.

# No caso dos operadores aritméticos, estes realizam operações matemáticas simples de acordo
# com o símbolo utilizado. Os operadores aritméticos em Python são:
# - Adição (+)
# - Subtração (-)
# - Multiplicação (*)
# - Divisão (/)
# - Potenciação (**)
# - Divisão inteira (//)
# - Resto de divisão (%)

# Assim como a matemática manual, os operadores possuem uma ordem de precedência:
# - 1º: parênteses ()
# - 2º: potência (**)
# - 3º: operações de natureza multiplicativa/divisora (*, /, //, %)
# - 4º: operações de natureza aditiva (+, -)

# Lembre-se: junta da ordem de precedência, a ordem de leitura de operações de mesma precedência
# ocorre da esquerda para a direita (ordem de leitura ocidental).

# Exemplo de operações aritméticas:

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = int(n1 + n2)
print(f'A soma entre {n1} e {n2} é igual a {soma}.')
print(f'A divisão da soma por {n1} é igual a {soma//n1}.')
print(f'A divisão da soma por {n2} é igual a {soma//n2}')

# Acima, pedimos ao usuário dois valores e atribuímos a soma destes a uma variável.
# Ademais, fizemos a divisão inteira da soma por cada um dos números.

# DICA: para calcular diversas raízes apenas com operadores matemáticos, utilize a lógica de potência:
# Um número elevado a uma fração é igual a raíz desta fração sobre um número.
# ex.: 81^(1/2) == raíz quadrada de 81.

# Veja o raciocínio abaixo:

numeroRaiz = int(input('Digite um número, e direi sua raíz quadrada: '))
raizQ = int(numeroRaiz**(1/2))
print(f'A raíz quadrada de {numeroRaiz} é igual a {raizQ}')

# Algumas operações matemáticas (adição e multiplicação) também funcionam com strings. Porém, ao
# invés de adicionar valores, será feita alguma alteração com o texto.

# Exemplo de operações com strings:

vezes = int(input('Escreva quantas vezes deseja repetir o asterisco: '))
print('*'*vezes)

# Ao executar a impressão de uma variável, é possível imprimir esta dentro de um determinado
# número de espaços. Útil para tabulação.

print('     TABELA DE VARIÁVEIS')
print(f'n1: {n1:>10}\nn2: {n2:>10}\nsoma: {soma:>10}\nnumeroRaiz: {numeroRaiz:>10}\nraizQ: {raizQ:>10}\nvezes: {vezes:>10}')

# Símbolos adicionais:
# - > = alinhamento à direita
# - < = alinhamento à esquerda
# - ^ = centralização

# Novos comandos 'print' automaticamente quebram linha. Para evitar isto, adicione o comando 'end=' e
# o símbolo que termina a frase.

print('Primeiro print', end='>>')
print('Segundo print')