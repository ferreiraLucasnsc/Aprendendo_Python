#       TUPLAS: VARIÁVEIS COMPOSTAS

# As variáveis simples conseguem armazenar apenas um dado. Fazendo uma nova atribuição, este dado anterior é apagado da memória e
# trocado pelo novo dado.
# Por mais que existam casos em que a troca de valores não é algo incômodo, algumas situações mais corriqueiras exigem múltiplos
# dados disponibilizados.

# Para tratar de diversos dados guardados em uma alocação da memória, utilizamos as variáveis compostas.

# TUPLAS: as tuplas são um tipo de variável composta que consegue armazenar diversos valores. Estes valores são alocados
# em diferentes espaços na memória, porém próximos a si, permitindo uma análise deses como um todo.

# Em variáveis compostas, diferentes elementos possuem índices (index) que os identificam. Os índices sempre começam com 0, então
# o primeiro elemento de uma variável composta possui o elemento 0. A partir daí, basta percorrer a variável até chegar ao seu limite.

# Exemplo: se temos a variável numeros = [1, 5, 22, 50]:
#   -   numeros[0] => 1                 numeros[-1] => 50 (-1 busca o último elemento; -2 busca o penúltimo; etc.)
#   -   numeros[1] => 5
#   -   numeros[2] => 22
#   -   numeros[3] => 50

# Assim como as cadeias (que são nada mais que variáveis compostas de múltiplos caracteres), podemos fazer a fatiação e diversas outras
# funcionalidades que vimos antes em strings.

# Podemos pedir o tamanho da tupla através de len(var). Aqui, len(numeros) => 4.

# Para tratar de variáveis compostas, podemos utilizar estruturas de repetição.
# Exemplo: podemos usar a seguinte sintaxe para mostrar cada número na nossa variável:
#       for n in numero:            ->  É criada uma variável SIMPLES de nome 'n', que recebe cada valor da variável composta, uma de
#           print(n)                    cada vez
#                                   ->  Ao realizar a impressão da variável, será mostrado na tela cada valor.
#       Como o primeiro valor é 1, n vale 1 na primeira passada. Ao repetir a estrutura, n perde este 1 e passa a valer 5, e assim
#       por diante.

# Em relação a execução do programa e à natureza das variáveis, uma tupla é IMUTÁVEL, ou seja, não pode ser modificada ao longo do 
# programa.
# Caso queira mudar o conteúdo de uma tupla, será necessária a parada do programa e a mudança no código.

#       === EXECUÇÃO PRÁTICA ===

'''print('\t\tExemplo de funcionamento de variável simples:')
lanche = 'Salgado'.upper()
print(f'Neste momento, a variável lanche tem o valor: {lanche}')
lanche = str(input('Porém, digite um lanche: ')).upper()
print(f'Agora, a variável lanche, que antes tinha o valor "SALGADO", agora tem o valor: {lanche}')
print('\t\t','='*100)'''

print('\t\tExemplo de tupla:')
lanche = 'HAMBÚRGUER', 'SUCO', 'DOCE'
print('A tupla lanche possui o seguinte valor:', lanche)
n = 0
for l in lanche:
    print(f'O lanche de número {n + 1} é: {l}')
    n += 1
print('O penúltimo item da tupla é:', lanche[-2])
print('A tupla criada possui', len(lanche), 'elementos')
print('A lista dos lanches:')
for pos, comida in enumerate(lanche):
    print('\t', comida, '\tPosição:', pos)

print(f'A tupla impressa na ordem alfabética é: {sorted(lanche)}')
print('\t\t', '='*100)

print('\t\tExemplo de operações com tuplas:')
conjA = (2, 5, 8, 9, 10)
conjB = (1, 3, 4, 6, 7, 2)
print(f'Conjunto A: {conjA}\tConjunto B: {conjB}')
adicao1 = conjA + conjB
print(f'\nAdição/junção de A + B: {adicao1}')
adicao2 = conjB + conjA
print(f'Adição/junção de B + A: {adicao2}')
print('\nEm ambas adições, o número 2 aparece', adicao1.count(2), 'vezes, enquanto o 10 aparece', adicao2.count(10))
print('Na primeira adição, o primeiro 2 aparece na posição', adicao1.index(2), 'e o segundo aparece na posição', adicao1.index(1, 2))
print('Na segunda adição, o primeiro 2 aparece na posição', adicao2.index(2), 'e o segundo aparece na posição', adicao2.index(5, 2))
print('\t\t', '='*100)

print('Exemplos de tuplas com diversos tipos de dados:')
pessoa = ('Lucas Ferreira', 19, 'M', 65)
print(pessoa)