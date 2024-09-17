#       MAIS SOBRE FUNÇÕES

# Anteriormente, vimos como funcionam as funções em nível básico: o que são, como funcionam e como podem ser implementadas em nossos
# códigos.
# A partir de agora, veremos particularidades mais avançadas das funções.

#   INTERACTIVE HELP

# A função 'help()' funciona como uma ajuda interativa entre a linguagem e os programadores.
# Esta função é nativa da linguagem, e ajuda a detalhar processos e casos da linguagem, colocando o que necessita de ser solucionado
# dentro dos parênteses.

# Aqui está um exemplo de uso da help():

'''print(f'{' LISTS EXPLANATION ':=^50}')
help(list)'''

# Veja que foi aberto um texto, em inglês, detalhando o elemento especificado. Caso a função seja chamada sem argumentos, será exibido
# um texto que permite visualizar diversas explicações, até que seja atingida uma condição de parada:

'''help()'''

# Esta documentação é bem útil para entender com mais detalhes funções e peculiaridades do Python.

# NOTA: o help() é mais usado para IDEs que não oferecem detalhes. Alguns, como o VSC, são explicativos - seja com ou sem extensões.
# ------------------------------------------------------------------------------------------------------------------------------------
#   DOCSTRINGS

# Seguindo a lógica da ajuda interativa, os docstrings são documentos textuais sobre alguns tópicos que podem ser exibidos. Ao usar o
# comando help() ou o comando print(///.__doc__), estamos buscando e exibindo documentações.
# O diferencial é que podemos criar docstrings sobre funções criadas por nós.

# Exemplo de uso de docstring:

#def contagem1(i, j, k):
#    '''
#            --- FUNÇÃO CONTAGEM ---
#        Realiza uma contagem utilizando três variáveis:
#         - i: valor inicial
#         - j: valor final
#         - k: passo das iterações
#        Nota: função sem retorno
#    '''
#    cont = i
#    while cont <= j:
#        print(cont, end='... ')
#        cont += k
#    print('\nFIM DA CONTAGEM')
# FUNÇÃO COM DOCSTRING

#def contagem2(i, j, k):
#    cont = i
#    while cont <= j:
#        print(cont, end='... ')
#        cont += k
#    print('\nFIM DA CONTAGEM')
# FUNÇÃO SEM DOCTRING

#help(contagem1)     # ajuda da função COM docstring
#help(contagem2)     # ajuda da função SEM docstring

# Perceba que a ajuda da contagem2 retornou nada. Isso é porque ela não tem uma docstring de ajuda. Ao criarmos nossa docstring, outras
# pessoas que utilizarem nosso programa, seja em nível de código ou apenas em uso, podem receber uma explicação detalhada sobre nossa
# função.
# -------------------------------------------------------------------------------------------------------------------------------------
#       PARÂMETROS OPCIONAIS

# Ao criar funções, podemos especificar quais parâmetros podem ficar vazios, ao atribuír para eles um valor na sua criação.
# Dessa forma, caso falte um argumento para este parâmetro, a função ainda funcionará. Se for digitado um argumento, o valor será
# simplesmente trocado.

# Aqui abaixo está um exemplo de função com parâmetros opcionais:

'''def soma(a=0, b=0, c=0):
    s = a + b + c
    print('A soma destes números é igual a:', s)
    print()

soma(2, 5, 10)
soma(3, 5)
soma(5)
soma()'''

# Em todas as ocasiões da função, não houve situação de erro. Isto ocorre pois existe os parâmetros opcionais, que já possuem valores
# atribuídos a eles.
# -----------------------------------------------------------------------------------------------------------------------------------
#       ESCOPO DE VARIÁVEIS

# Com a possibilidade de funções, nem sempre as variáveis serão acessíveis normalmente. Isso ocorre porque não são do mesmo ESCOPO.
# O escopo é o local contextual na memória onde as variáveis são armazenadas. Caso uma variável esteja em um escopo que não pode
# ser alcançado, logo ela também não estará.
# Dependendo do local onde declarada, uma variável pode pertencer a um diferente local.

# Existem dois escopos para uma variável: GLOBAL e LOCAL.
# Uma variável global é declarada no código principal e vale para todo o código, podendo ser revisada ou impressa a qualquer momento.
# Uma variável local é declarada em uma porção específica do código (ex.: uma função) e vale SOMENTE para aquela região. Se a variável
# for chamada fora desta região, o programa não apresentará, pois está em um escopo diferente.

# Abaixo segue um exemplo claro de escopos:

'''def amostraEscopo():
    x = 10
    print('Na função amostraEscopo, x vale', x)
    print('Na função amostraEscopo, n vale', n)

n = 5
print('No programa principal, x vale', x)
print('No programa principal, n vale', n)
amostraEscopo()'''

# No VSC, o problema já foi apontado. Em outras IDEs, ao executar o código, aparece o erro de uma variável não identificada.
# A variável n foi declarada na - digamos - função principal, o código principal. Assim, ela vale para todo o código, incluindo
# a função (lembre: no caminho de execução de código, o principal é primeiro, e depois as funções).
# A variável x, porém, não existe fora da função, pois foi declarada dentro dela. Assim, ela vale apenas para a função.

# Sobre o funcionamento de escopos, podemos ter DUAS VERSÕES de uma variável, declarando ela uma vez no código global e outra no
# código local:

'''def testes():
    a = 8
    print('A variável a dentro da função vale', a)

a = 5
print('A variável a fora da função vale', a)
testes()'''

# Por fim, assim como as variáveis têm escopos, as chamadas de BIBLIOTECAS também possuem escopos global e local. Cada biblioteca
# funcionará em cada escopo que pertence.

# Para evitar que uma variável global receba uma duplicada local, podemos adicionar a frase 'global ---' para continuar valendo
# a variável:

'''def testes():
    global a
    a = 8
    print('Dentro da função, a vale', a)

a = 5
print('Fora da função, antes de chamar a função, a vale', a)
testes()
print('Fora da função, depois de chamar a função, a vale', a)'''
# --------------------------------------------------------------------------------------------------------------------------------
#       RETORNO DE VALORES

# A maioria das funções criadas até agora não retornavam nenhum valor. Todos os processos eram executados ali e as impressões de
# mesmo modo.

# Porém, podemos retornar valores das funções, para realizarmos processos com os resultados das funções.

# O retorno de um valor é atribuído ao que vem antes dele. Assim, podemos atribuir o resultado de uma função à uma variável.

# Abaixo segue um exemplo do retorno de valores:

'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

respostas = list()
respostas.append(somar(2, 4, 6))
respostas.append(somar(2, 4))
respostas.append(somar(2))
print(f'As três somas realizadas são {respostas[0]}, {respostas[1]} e {respostas[2]}')'''

# Como a função retorna valores, não apenas podemos atribuir um resultado a uma variável, como podemos atribuir diversos resultados
# à diversas variáveis ou - como foi feito aqui em cima - à uma lista.