#       TRATAMENTO DE ERROS E EXCEÇÕES

# Um dos casos mais recorrentes em programas, seja qualquer linguagem em que são escritos, são erros. Várias vezes, por vários motivos,
# algo inesperado acontece em nosso programa, que faz com que seja exibida uma mensagem de erro e o fechamento repentino do programa.

# O que os programadores necessitam fazer é estarem preparados para a ocasião desses erros acontecerem. Como erros são comuns,
# um bom programa é aquele que foi planejado de uma forma que consiga evitar ou tratar estes erros.

# Um exemplo de erro comum é a impressão do que era pra ser uma variável, mas que não tem variável nenhuma:

'''print(x)'''

# O simples comando acima nos retornou um erro: a variável 'x' não foi definida, logo ela não pode ser impressa.

# Geralmente, as mensagens de erro nos fornecem os dados necessários para corrigí-lo. Vamos ver a mensagem exata do erro acima:

# Traceback (most recent call last):
#   File "c:\Users\lucas\Arquivos VSC\Aprendendo Python\Códigos de anotação\Módulo 3\16-09-2024\16092024-01.py", line 17, in <module>
#     print(x)
#           ^
# NameError: name 'x' is not defined

# Vejamos o que está escrito nesta mensagem:
# - No arquivo 16092024-01.py, na linha 17, ocorre um erro quando é feito o módulo (execução)
# - O erro está no 'x' do comando 'print(x)', como visto na sinalização apontando para o 'x' (^)
# - O erro é especificamente um erro de nome, pois está destacado 'NameError', uma palavra que detalha a categoria do erro
# - O erro em si ocorre porque o nome 'x', no nosso caso, uma variável, não foi definida

# Neste caso, não temos um erro de sintaxe (comando escrito de forma errada), mas um erro semântico (casos de erro com dados),
# este erro recebe o nome de EXCEÇÃO. O erro acima foi exatamente isso: o comando 'print()' está escrito correto, logo funciona.
# Porém, aconteceu o caso de uma variável não definida. O comando funciona, com exceção deste caso.

# Vejamos um outro erro comum:

# n = int(input('Escreva um número: '))
'''n = int('cinco')
print(f'Você digitou o número {n}')'''

# O programa esperava um número inteiro, porém recebeu uma palavra. Veja a mensagem de erro desta situação:

# Traceback (most recent call last):
#   File "c:\Users\lucas\Arquivos VSC\Aprendendo Python\Códigos de anotação\Módulo 3\16-09-2024\16092024-01.py", line 36, in <module>
#     n = int('cinco')
#         ^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'cinco'

# Agora, o tipo de erro é um erro de valor (ValueError). Ou seja, o erro está no dado que foi atribuído para a variável.
# Aqui, atribuímos uma cadeia de caracteres à uma variável de números inteiros.

# Veja este caso curioso de erro:

'''denominador = 8
numerador = 0
resultado = denominador / numerador
print(f'A divisão {denominador}/{numerador} retorna o valor {resultado}')'''

# Temos todas as estruturas corretas, mas ainda recebemos um erro. Vamos ver a mensagem:

# Traceback (most recent call last):
#   File "c:\Users\lucas\Arquivos VSC\Aprendendo Python\Códigos de anotação\Módulo 3\16-09-2024\16092024-01.py", line 54, in <module>
#     resultado = denominador / numerador
#                 ~~~~~~~~~~~~^~~~~~~~~~~
# ZeroDivisionError: division by zero

# O erro está na divisão: um dos números que participam da divisão é o número 0. Na matemática, nenhum número pode ser dividido por 0.
# Com atribuímos ao 0 o papel do numerador, cometemos um erro matemático (ZeroDivisionError).

# Assim por diante, existem vários tipos de exceções.

# Existem dois comandos que nos permitem tratar os erros que podem acontecer: 'try' e 'except'.

# Os próprios nomes dizem por si, mas vamos detalhar cada um:
# - try: estrutura que testa uma operação que pode receber um erro ou não
# - except: estrutura que trata a exceção acontecida. Escrevemos ele junto com o tipo da exceção

# Vamos testar um código com os comandos 'try' e 'except':

'''try:
    a = int(input('Digite um denominador inteiro: '))
    b = int(input('Digite um numerador inteiro: '))
    r = a / b
    print(f'A divisão {a}/{b} é igual a {r}')
except:
    print('Algo de errado ocorreu nesta divisão')'''

# Aqui, usamos um 'try' para a nossa expressão normal. Como usamos um 'except' geral, sem a especificação de uma exceção específica,
# QUALQUER exceção vai executar a porção do código na estrutura 'except'.

# Além do 'try' e 'except', temos outros dois comandos:
# - else: código executado se não for retornado um erro
# - finally: código que é executado independente de erro ou sucesso

# Vamos criar um código completo: teste, exceção, caso de nenhuma exceção e mensagem independente:

'''try:
    a = int(input('Digite um denominador inteiro: '))
    b = int(input('Digite um numerador inteiro: '))
    r = a / b
except ValueError:
    print('Valores errados!')
except ZeroDivisionError:
    print('Zero (0) não pode ser divisor!')
except:
    print('Erro no programa!')
else:
    print(f'A divisão {a}/{b} é igual a {r:.1f}')
finally:
    print('Fim da execução do bloco')'''

# Aqui, além de criarmos blocos para diferentes exceções, temos o caso de nenhuma exceção e a mensagem exibida normalmente.

# Podemos exibir o erro, ao usarmos a classe 'Exception' como um dado de variável:

'''try:
    a = int(input('Digite um denominador inteiro: '))
    b = int(input('Digite um numerador inteiro: '))
    r = a / b
except Exception as erro:
    print(f'Erro no programa: {erro.__class__}')
else:
    print(f'A divisão {a}/{b} é igual a {r:.1f}')
finally:
    print('Fim da execução do bloco')'''