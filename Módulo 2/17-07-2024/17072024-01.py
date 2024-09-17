#       LAÇOS DE REPETIÇÃO

# Até agora, vimoas as estruturas condicionais, que levam em consideração certas condições e
# fluxos diferentes.
# Existem casos, porém, onde temos que testar esta condição por um tempo indeterminado. Ou
# por um tempo longo.

# Para evitar a repetição de várias estruturas, usamos as estruturas de repetição. As estrutuas
# de repetição testam condições por um certo número de iterações.
# Esta estrutura de repetição, nós chamamos de laços (ou loops), que possuem este nome devido
# ao seu fluxo ter a forma de um laço:

# CONDIÇÃO -> codigo1 -> FIM    =>  condição verdadeira
#     |                   ^
#     V                   |
# codigo2       ->        O     =>  condição falsa

# A diferença é que, nos laços de repetição, devemos adicionar uma atualização para a variável
# que compõe a condição.
# Se um laço trata uma condição que sempre será verdadeira ou sempre será falsa, criamos um
# loop infinito, ao invés de um laço de repetição.

#   ESTRUTURA 'FOR':

# A estrutura for se trata de um laço de repetição que repete por um tempo DETERMINADO de iterações.
# A sintaxe da estrutura FOR é esta:
#   for var in range(..):
#       - - -

# SIGNIFICADO: temos um laço que trata uma variável, que vai de um valor até outro valor (range).

# Exemplo de estrutura FOR:

print('Contagem regressiva para o lançamento:')
contagem = 10
for c in range (10, 0, -1):
    print(f'{contagem}...')
    contagem = contagem - 1
print('Lançamento concluído!!')

# Aqui, adicionamos mais um número no comando range: passo.
# O passo é como a variável de controle é atualizada: de 1 em 1, de 5 em 5, regressando de 1 em 1...
# Valores positivos aumentam a contagem, enquanto valores negativos diminuem a contagem
# O padrão é que o valor seja 1. Sem a adição de um passo específico, o passo será igual a 1.

# Podemos adicionar variáveis já criadas para nossas iterações:

passo = int(input('Digite um número: '))
print(f'Contando de 0 até 20, de {passo} em {passo}:')
for c in range (0, 20, passo):
    print(f'{c}...')
print('Contagem concluída!!')