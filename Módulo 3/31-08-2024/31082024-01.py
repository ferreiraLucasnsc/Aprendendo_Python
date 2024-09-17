#   MÓDULOS E PACOTES

# Em Python, módulos são arquivos que contêm em seu código-fonte funções e outros elementos, como classes e variáveis.
# Agrupar um código específico para uma tarefa (ex.: funções e classes) em um código externo melhoram a visibilidade do
# seu programa, além de deixar o processo de codificação mais organizado.

# Para criar um módulo, basta criar um novo arquivo Python e importar este arquivo. Abaixo, segue o exemplo de um módulo
# para cálculos:

'''import calc
msg = '  CALCULADORA'
lenMsg = len(msg) + 2
print(msg)
print('-' * lenMsg)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('    Qual será a operação?')
print(' 1 - Adição')
print(' 2 - Subtração')
print(' 3 - Multiplicação')
print(' 4 - Divisão')
esc = str(input(' : '))
res = 0
if esc == '1':
    res = calc.adicao(n1, n2)
elif esc == '2':
    res = calc.subtracao(n1, n2)
elif esc == '3':
    res = calc.multiplicacao(n1, n2)
elif esc == '4':
    res = calc.divisao(n1, n2)
if res != 0:
    print('O resultado é:', res)
else:
    print('Não houve operação')'''

# Criamos o arquivo calc.py, que possui as funções dos cálculos. Em seguida, importamos o arquivo para usar suas funções pela sintaxe
# xxx.yyy, onde x = nome do arquivo e y = função. Podemos também usar o from xxx import yyy, para escolher funções específicas.

# Existem módulos nativos do Python que já utilizamos. Alguns deles são:
# - pi (biblioteca math)
# - randint (biblioteca random)
# - time() (biblioteca time)

# Se houver a necessidade de usar vários módulos para diferentes tarefas, podemos utilizar os pacotes. Os pacotes são pastas que
# guardam diferentes módulos para diferentes ocasiões.
# Pacotes podem receber subpacotes para diferentes momentos do código, aumentando a organização do nosso programa.

# Para que uma pasta seja reconhecida como pacote pelo Python, ela deve conter um arquivo '__init__.py'. O arquvio pode estar
# vazio ou com um código de inicialização, mas ele DEVE estar presente na pasta, para que ela seja recebida como pacote:

'''from modulos.fator.fatorial import fatorial
from modulos.poten.potencia import potencia
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
res = 0
print('    Qual será a operação a ser realizada?')
print(' 1 - Fatorial (primeiro número)')
print(' 2 - Fatorial (segundo número)')
print(' 3 - Potência')
esc = str(input(' : '))
if esc == '1':
    res = fatorial(n1)
elif esc == '2':
    res = fatorial(n2)
elif esc == '3':
    res = potencia(n1, n2)
if res != 0:
    print('O resultado da operação é:', res)
else:
    print('Não houve operação')'''

# Na importação, colocamos o endereço absoluto do pacote. Podemos também colocar endereços relativos:

'''from modulos.fator import fatorial
from modulos.poten import potencia
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
res = 0
print('    Qual será a operação a ser realizada?')
print(' 1 - Fatorial (primeiro número)')
print(' 2 - Fatorial (segundo número)')
print(' 3 - Potência')
esc = str(input(' : '))
if esc == '1':
    res = fatorial.fatorial(n1)
elif esc == '2':
    res = fatorial.fatorial(n2)
elif esc == '3':
    res = potencia.potencia(n1, n2)
if res != 0:
    print('O resultado da operação é:', res)
else:
    print('Não houve operação')'''