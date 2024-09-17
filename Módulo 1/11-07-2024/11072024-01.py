#       MANIPULAÇÃO DE TEXTO

# Cadeias (ou strings) são sequências de caracteres variados. Espaços em branco, símbolos, números e
# letras são caracteres que compõem estas cadeias.
# Valores de cadeia aparecem sempre entre aspas, simples ou duplas. As aspas são delimitadores que
# especificam o comprimento de uma cadeia.

# Veja a seguinte atribuição:

frase = str('Estou programando em Python')
print(frase)

# A variável frase recebe o valor 'Estou programando em Python!'.
# Quando uma cadeia é atribuída a uma variável, a cadeia é dividida em pedaços para serem guardados
# na memória do computador. Cada caracter é um espaço guardado, incluindo os espaços vazios.

# Assim como uma lista, ou uma matriz, cada item de uma cadeia possui um índice que destaca a posição
# dele. Os índices começam do número 0, e vão até chegar ao final da cadeia.
# A frase 'Estou programando em Python!' tem como índice máximo 27 (28 letras que iniciam no 0).

# Abaixo, serão detalhadas algumas alterações ou funções que podem ser realizadas com cadeias.

#   FATIAMENTO

# O fatiamento de uma cadeia consiste em pegar um pedaço dela de acordo com o índice.
# Podemos fazer o fatiamento de duas formas: pedaço único, ou área.
# Para pegar um pedaço, escrevemos o nome da variável[indice].

# Exemplo de fatiamento único:

print(f'A décima letra da frase acima é {frase[9]}.')

# Aqui, nós pegamos a décima letra da frase (como o primeiro índice é 0, a décima letra é a 9 (10-1=9))

# Exemplo de fatiamento de área:

print(f'A segunda palavra da frase acima é {frase[6:17]}.')

# Aqui, pegamos uma área que, no caso da nossa frase, equivale a segunda palavra.
# Extendemos a área para além da última letra, pois o último índice é excluído.

# Você também pode ir com um número de passo ao adicionar um terceiro índice.

# Exemplo de fatiamento com passo:

print(f'Pulando de 2 em 2, a segunda palavra fica {frase[6:17:2]}.')

# Para ir do começo até um certo índice, basta excluir o primeiro índice (ou escrevê-lo como 0, mas
# não é necessário. Então, excluímos o primeiro índice):

print(f'A primeira palavra é {frase[:5]}.')

# Da mesma forma, excluímos o último índice para ir de um ponto até o final:

print(f'A última palavra é {frase[21:]}.')

# Excluíndo apenas o segundo, indicamos o ponto de partida e o passo:

print(f'Pulando de 3 em 3, a última palavra fica {frase[21::3]}.')

#   ANÁLISE

# Na análise, trabalhamos com os dados sobre a cadeia. Qual o seu comprimento, seu caracter inicial, seu
# caracter final, e outros, são dados analisados.S

# Para descobrimos o tamanho de uma cadeia, utilizamos a função len(variavel):

print(f'O tamanho da frase é de {len(frase)} caracteres.')

# Podemos contar quantas vezes se repete um determinado caracter pelo variavel.count('char'):

print(f'Na frase, existem {frase.count('a')} letras A.')

# Você pode adicionar índices separados em vírgula para fazer a contagem fatiada:

print(f'A segunda palavra somente tem {frase.count('o', 6, 17)} letras O.')

# Podemos procurar certos trechos usando variavel.find('trecho'):

print(f'Encontramos o trecho "amando" no lugar {frase.find('amando')}.')

# Caso procure um trecho inexistente, será retornado o valor -1.

# Para saber se existe um trecho na frase, usamos o operador 'trecho' in variavel:

print(f'Existe a palavra "código" na frase? {'código' in frase}.')

#   TRANSFORMAÇÃO

# Podemos fazer alterações diversas nas cadeias que estamos tratando.

# Para substituir pedaços da frase, usamos o método frase.replace('aaa', 'bbb'):

print(f'\n{frase.replace('programando em', 'aprendendo')}.')

# Podemos usar as funções .upper() e .lower() para alterar todas as letras para caixa alta ou baixa:

print(f'{frase.upper()}\n{frase.lower()}')

# Ou capitalizar/titular a frase:

print(f'{frase.capitalize()}\n{frase.title()}')

# Em casos de espaços antes da primeira letra da frase, usamos .strip() para tirar estes espaços:

frase2 = str('       Muitos espaços!        ')
print(f'{frase2}\t=>\t{frase2.strip()}')

# Podemos especificar o lado dos espaços ao adicionar as letras l(eft) ou r(ight):

print(f'{frase2.lstrip()}\n{frase2.rstrip()}')

#   DIVISÃO E JUNÇÃO

# Podemos pegar uma cadeia grande e dividir ela em outras menores:

# O comando .split() separa a cadeia em seus espaços:

fraseSplit = frase.split()
print(fraseSplit)

# Para juntar a frase, usamos 'char'.join(variavel):

lista = ['Marcos', 'Antônio', 'Carlos', 'Joana']
print(lista)
print(f'A junção desta lista com o caracter + é:\n{' + '.join(lista)}\n\n')

# Para fazer a impressão de um texto com quebras de linha, adicionamos três aspas duplas:

print("""Olha só que texto longo, como esse texto é longo. Eu não sei se eu vou conseguir imprimir
ele inteiro com apenas um comando print. Eu não quero ter que colocar diversos prints no meu
código porque isso não é uma coisa boa. Uma vez eu vi que pra dar um print só de um texto bem
longo, é só você colocar três aspas duplas no texto e dá certo. Mas será que dá mesmo? Eu nunca
vi isso nas outras linguagens, mas mesmo assim eu vou tentar. Se der certo eu volto e falo aqui
com vocês.""")