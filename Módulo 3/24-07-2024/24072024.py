#       LISTAS: VARIÁVEIS COMPOSTAS

# Assim como as tuplas, as listas são uma forma de variáveis compostas. O diferencial entre ambas é que as listas - ao
# contrário das tuplas - podem ser modificadas.

# Exemplo: crio a lista numeros = [1, 3, 5, 10]. Posso executar o seguinte comando sem erros:
#       numeros[2] = 6
# Agora, a lista numeros = [1, 3, 6, 10]
#       Com listas, podemos modificar o conteúdo dentro das variáveis compostas:

'''print('Para o estudo de listas, foi criada a seguinte variável:')'''
# numeros = [1, 3, 5, 10]
'''print(numeros)
print()
i = int(input('Escolha a posição do item para ser trocado: '))
numeros[i - 1] = int(input('Agora, digite o novo valor desta posição: '))
print('Agora, a nova lista é:')
print(numeros)
print()'''

# Além de TROCAR valores, podemos ADICIONAR valores, através do comando '.append(...)':

# print('Antiga lista:', numeros)
'''new = int(input('Digite o novo valor a ser adicionado: '))
numeros.append(new)
print('O objeto foi adicionado à lista:')
print(numeros)
print()'''

# Podemos especificar o local do novo item, usando '.insert(i, ...)':

'''i = int(input('Escolha o local em que deseja adicionar o valor: '))
new = int(input('Agora, digite o novo valor a ser adicionado: '))
numeros.insert(i - 1, new)
print('Agora, a nova lista é:')
print(numeros)
print()'''

# Assim como adicionamos, podemos APAGAR elementos de duas formas:
# - simples: comando del ...[i] ou '.pop[i]':

'''i = int(input('Escolha a posição do item que deve ser apagado: '))
del numeros[i - 1]
print('Agora, a nova lista é:')
print(numeros)
print()'''

# - específico: comando '.remove[...]':

'''tirar = int(input('Digite o valor que deseja retirar: '))
if tirar in numeros:
    numeros.remove(tirar)
    print('Agora, a nova lista é:')
    print(numeros)
else:
    print('Este item não está na lista, portanto não pode ser retirado')'''

# Usar o comando pop() vazio retira o ÚLTIMO item da lista

# Assim como a tupla, podemos delcarar variáveis compostas através de funções:
# - tupla: tuple(...)
# - lista: list(...)

'''listaUser = list(int(input('Digite um valor: ')) for i in range(0, 5))
print('A lista que você criou é:', listaUser)'''

# Podemos ordenar as listas, através do '.sort()' ou do comando sorted(...):

nomes = ['João', 'Ana', 'Zélia', 'Ricardo', 'Vinícius']
'''print('Lista não ordenada:', nomes)
print('Lista ordenada:', sorted(nomes))'''

# len(...) = tamanho da lista

'''print('A lista NOMES tem', len(nomes), 'nomes escritos:', nomes)'''