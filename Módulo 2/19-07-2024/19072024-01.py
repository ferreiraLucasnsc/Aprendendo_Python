#       INTERROMPENDO ESTRUTURAS WHILE

# Para adicionar uma camada de complexidade e reiqueza ao nosso programa, podemos adicionar uma
# condição especial à estrutura WHILE que a interrompa por completo, mesmo se a condição inicial
# ainda estiver sendo testada como verdadeira.
# Neste caso, temos a opção de adicionar um comando de interrupção, que termina o laço no momento
# em que a linha onde ele se localiza é lida e executada pelo programa.

# Em algoritmos em português, temos o comando 'interrompa'. Como o Python foi feito no vocábulo
# inglês, temos o comando 'BREAK'.

# Veja este código:

n = 0
while n != 999:
    n = int(input('Digite um número, ou digite 999 para encerrar: '))
print('Contagem interrompida.')

# Podemos fazer este código de uma forma diferente, sem uma condição, e usando o comando 'break':

print('='*130)
n = 0
while True:
    n = int(input('Digite um número, ou digite 999 para encerrar: '))
    if n == 999:
        break
print('Contagem interrompida.')

# Ao declararmos o WHILE com a condição TRUE (apenas verdade), estariamos criando um loop infinito, se não
# tivesse a condição abaixo para interromper a estrutura.

# Este método é útil quando em nosso programa existir uma flag (valor de variável que termina o laço), e devemos
# ignorar o valor desta flag.