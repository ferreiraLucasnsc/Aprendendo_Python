#       FUNÇÕES

# Funções são estruturas que realizam uma determinada rotina, determinados passos ordenados, sempre que chamada.
# Sem percebermos, usamos muitas funções nas aulas passadas de Python. print(), input(), int() e outras são funções
# nativas da linguagem de programação.

# Quando as funcionalidades nativas não conseguem satisfazer nossas necessidades, entretanto, podemos também criar as
# nossas próprias funções, determinando os processos e as variáveis que serão tratadas pela função.

# Para criar nossa função, definimos seus detalhes através do comando 'def', escolhemos o nome com o sufixo '()'.
# Estes parênteses podem ser vazios, quando a função não necessita de variáveis, ou contendo dados.

# Um exemplo de função: criando uma função que exibe linhas para melhorar a visibilidade do programa:

'''def mostrarLinhas():                            # Comando para criar a função
    print('=' * 50)                             # Rotina executada pela função

mostrarLinhas()                                 # Chamada da função para executar seus passos
print(f'{'FUNÇÃO CRIADA E SENDO USADA':^50}')
mostrarLinhas()                                 # Chamada da função para executar seus passos
'''

# Como dito anteriormente, os parênteses podem estar vazios quando a função não precisa de tratar variáveis.
# Na maioria dos casos, as funções tratam dados dentro de suas rotinas.
# Neste caso, colocamos um parâmetro dentro dos parênteses, e podemos utilizá-lo dentro da rotina.

# O diferencial das funções com parâmetros é que podemos atribuir qualquer valor à este elemento, ao inserir um valor
# na chamada da função.

# Exemplo: modelo de caixa para apresentação de mensagens:

'''def mensagem(msg):                               # Função com parâmetro definido
    print('=' * 50)
    print('||', end='')
    print(f'{msg:^46}', end='')                     # Local de uso da variável
    print('||')
    print('=' * 50)

mensagem('MENSAGEM EXIBIDA COM SUCESSO')            # Função chamada com argumento
'''

# Parâmetros são variáveis especificadas dentro dos parênteses da função, representando os dados esperados quando uma função
# é chamada, usando estes valores na rotina da função.
# Quando uma função é chamada com um valor atrelado, ela recebe um argumento. Este argumento é compreendido como valor do
# parâmetro e, ao receber o argumento, a função realiza seus processos com o argumento.

# Importante notar que a quantidade de argumentos precisa ser a mesma de parâmetros. Se uma função possui dois parâmetros, devem
# ser retornados dois argumentos.

# Exemplo de função: cálculo de potência:

'''def potenciacao(num, pot):
    cont = 0
    res = 0
    if pot == 0:
        res = 1
        return res
    while True:
        num *= num
        cont += 1
        res = num
        if cont == pot:
            break
        return res

print(f'{' CÁLCULO DE POTÊNCIA ':=^50}')
numero = int(input('Digite a base da potência: '))
exp = int(input('Digite o expoente da potência: '))
resultado = potenciacao(numero, exp)
print('A potência', numero, '^', exp, '=', resultado)'''

# Uma particularidade do Python é que você consegue, sim, trabalhar com quantidades distintas de argumentos e parâmetros:
# def ---(*///) ->  O sinal de asterisco desempacota os argumentos e armazená-los dentro de um parâmetro

# Exemplo: impressão dos valores:

'''def contador(*num):
    for valor in num:
        print(valor, end='  ')
    print('Fim dos valores')
    tam = len(num)
    print('Ao todo, foram informados', tam, 'números')

contador(1, 2, 3, 4, 5)
contador(3)
contador(3, 6, 8, 10, 50, 45, 60, 100, 59)'''

# Neste caso, o parâmetro se torna uma tupla, e podemos realizar as operações de tuplas.
# Caso seja necessário, podemos trabalhar com as listas também:

'''def dobrarLista(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [1, 2, 3, 4, 5]
print('A lista original é:', valores)
dobrarLista(valores)
print('A lista dobrada é', valores)'''

# Aqui, também aprendemos que as mudanças feitas na função permanecem na variável original.