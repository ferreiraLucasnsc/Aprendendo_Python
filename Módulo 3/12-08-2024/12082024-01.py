#       DICIONÁRIOS

# A terceira estrutura de variáveis compostas, os dicionários têm como principal destaque os índices personalizáveis.
# Ao contrário das tuplas e listas, que tinham os índices como apenas números iniciando do 0, os dicionários podem receber novos valores
# para servirem como índices.

# Observe o exemplo abaixo:

'''dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print('Nome:', dados['nome'])
print('Idade:', dados['idade'])'''

# Aqui, escolhemos o item do nosso dicionário através do índice que decidimos (no caso, as palavras 'nome' e 'idade'). Estes termos servem
# como índices e, quando especificados, permitem operações assim como os índices numéricos.
# Da mesma forma, podemos adicionar elementos a partir dos índices:

'''dados['sexo'] = 'M'
print('Sexo:', dados['sexo'])
print(dados)'''

# Adicionamos um novo dado ao dicionário a partir de um novo índice.

# Assim como nas listas, podemos apgar elementos usando os índices dos termos:

'''dados['nome'] = 'Maria'
dados['idade'] = 15
del dados['sexo']

print()
print('Nome:', dados['nome'])
print('Idade:', dados['idade'])
print(dados)
print()'''

# Um dicionário possui três elementos: valores, chaves e itens.
#   - Valores são aquilo que está guardado, relacionado a um índice. Se {'nome': 'Lucas'}, 'Lucas' é o VALOR.
#   - Chaves são os termos que determinam o índice do valor. Com {'nome': 'Lucas'}, 'nome' é a CHAVE.
#   - Itens são ambas chaves e valores. Em {'nome': 'Lucas'}, ' 'nome': 'Lucas' ' é o ITEM

# Observe abaixo a diferenciação entre os três:

'''dados = {'nome': 'João', 'idade': 27, 'curso': 'Engenharia'}
print('Valores:', dados.values())
print('Chaves:', dados.keys())
print('Itens:', dados.items())'''

# Usando estes conceitos, podemos imprimir dicionários da mesma forma que imprimimos listas:

# Listas:

'''lista = [1, 2, 4, 7, 9, 12, 15, 20]
for i, j in enumerate(lista):       # i recebe os índices (enumerate retorna índices) e j recebe os valores
    print(f'O {i+1}º termo é {j}')
print()'''

# Dicionários:

'''dici = {0: 1, 1: 2, 2: 4, 3: 7, 4: 9, 5: 12, 6: 15, 7: 20}
for a, b in dici.items():           # a recebe os índices (.items retorna índices) e b recebe os valores
    print(f'O {a+1}º termo é {b}')'''

# Porém, com as listas, podemos especificar os índices:

'''filme = {'titulo': 'Jumanji', 'ano': 2019, 'diretor': 'Jake Kasdan'}
print('     ANÁLISE DE FILMES')
for chave, item in filme.items():
    print(f'O {chave} do fime é: {item}')'''

# Podemos criar listas que recebem como itens dicionários, aumentando a complexidade dos nossos programas