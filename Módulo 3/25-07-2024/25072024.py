#       CONTINUAÇÃO DE LISTAS

# Na aula passada, vimos que usando a sintaxe 'var[:]', criamos uma cópia dos elementos de uma determinada lista:

'''lista1 = [1, 2, 3, 4, 5]
print('Lista 1:', lista1)
lista2 = lista1[:]
print('Lista 2 (cópia de Lista 1):', lista2)
lista3 = lista1
print('Lista 3 (ligação com Lista 1):', lista3)'''

# Usando cópias, podemos alterar listas existentes a partir de outras, mas sem modificar as originais:

'''print('\nAdicionando o número 10 nas listas 2 e 3:')
lista2.append(10)
lista3.append(10)
print('Lista 1:', lista1)
print('Lista 2 (cópia de Lista 1):', lista2)
print('Lista 3 (ligação com Lista 1):', lista3)'''

# PERCEBA: como as listas 3 e 1 estão ligadas por atribuição, o que ocorre em uma ocorre na outra. A lista 2 não é assim.
# A lista 2, por ser uma cópia, pode ser alterada, que não afetará a lista original.

# Usando este método de cópias, podemos fazer a adição de ESTRUTURAS em outras listas:

'''pessoas = list()
print('Pessoas:', pessoas, '\t\t\tVAZIA')
dados = ['João', 25]
print('Dados:', dados, '\t\tDADOS A SEREM ADICIONADOS')
pessoas.append(dados[:])
print('Pessoas:', pessoas, '\tLISTA COM CÓPIA DE DADOS')'''

# No exemplo acima, adicionamos uma lista DENTRO de outra lista. Podemos fazer isso mais de uma vez:

'''dados1 = ['Maria', 52]
dados2 = ['Rafael', 19]
pessoas.append(dados1[:])
pessoas.append(dados2[:])
print('Pessoas:', pessoas)'''

# Podemos criar novas estrutras através do método convencional, abrindo novos colchetes a cada nova estrutura:

'''pessoas = [['João', 20],
           ['Maria', 17],
           ['Marcos', 37]]
print('Pessoas:', pessoas)'''

# Usando a lista passada, podemos fazer tratamentos de listas contendo listas:
# Para buscar uma informação específica, evidenciamos o índice da lista buscada e o índice da informação desejada:

'''print('Idade da segunda pessoa:', pessoas[1][1])  # [1] -> segunda LISTA; [1] -> segundo ITEM da segunda LISTA'''

# Assim, podemos - usando uma variável - adicionar várias estruturas:

'''pessoas = list()
dado = ['Gustavo' , 32]
pessoas.append(dado[:])
dado = ['Maria', 24]
pessoas.append(dado[:])
dado = ['Marcos', 19]
pessoas.append(dado[:])'''
'''print(pessoas)'''

# Podemos exibir as informações com uma melhor formatação:

'''for pessoa in pessoas:                                      # pessoa = variável que recebe as listas internas
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')'''     # [0] e [1] = índices da pessoa (lista interna)

# Vamos pedir para o usuário adicionar três pessoas, com nome e idade:

'''pessoas = list()
dado = list()
for i in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:])
    dado.clear()
    print('----------------------------------')
print('Lista criada:')
for p in pessoas:
    print(f'Nome: {p[0]}\tIdade: {p[1]}')'''