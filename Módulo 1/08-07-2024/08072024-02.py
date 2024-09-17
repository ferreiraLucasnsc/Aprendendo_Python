#   PRIMEIROS COMANDOS EM PYTHON

# Comando 'print': serve para exibir na tela aquilo que está especificado dentro dos parênteses.
# No caso de mensagens de texto, estas devem ser delimitadas por aspas (duplas ou simples). Números
# não precisam seguir estas delimitações, ainda mais caso estes recebam algumas operações.

# Exemplo do comando 'print':

print('Olá, mundo!')

# O comando acima fez com que a frase "Olá, mundo!" fosse exibida na tela do terminal.

# Segundo exemplo, desta vez com operação entre números:

print('O resultado da adição entre 10 e 15 é', 10 + 15)

# Aqui, foi exibida a mensagem de texto e, ao lado, a operação de adição retornando o valor.

# Variáveis: objetos que recebem diversos valores. Na declaração de uma variável em Python, o nome
# desta precisa seguir a regra dos nome de variáveis (sem símbolo, inicia minúscula, sem espaço branco)
# Para assinalar uma variável a um valor, utilizamos o símbolo da igualdade.

# Exemplo de variável e sua exibição:

nome = 'Lucas'
print('Olá,', nome)

# Aqui, atribuímos o valor 'Lucas', um texto, à variável nome. Em seguida, exibimos o valor dela ao
# digitar o nome da variável sem aspas, buscando o valor dela no momento.

# Valores atribuídos ficam reservados na memória do computador, podendo serem acessados para diversos fins.

# Comando 'input': esta função lê um valor digitado pelo usuário. Este é o primeiro passo de um programa
# interativo com o usuário. O comando deve ser atribuído a uma variável, para que o valor digitado pelo
# usuário tenha algum local para ser armazenado.

# Exemplo do comando 'input':

nome = input('Qual é o seu nome? ')
print('Sendo assim, olá,', nome, '!')

# O comando 'input' permite uma mensagem antes da leitura de um valor. Após digitado, o valor foi
# atribuído a variável nome, e o novo valor dela foi exibido na tela.