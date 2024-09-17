#       CORES NO TERMINAL

# Para deixar nossos programas mais atraentes, podemos adicionar cores a certos elementos em
# nosso terminal, que exibe por padrão letras brancas em um fundo preto.

#   PADRÃO ANSI
# O padrão ANSI é um padrão de normalização (assim como a ABNT exige um padrão de formatação) focado
# na sequência de escape - ou seja - nos elementos exibido no terminal.

# Sempre que for necessária a adição de uma nova cor, usamos o prefixo '/033[1; 2; 3m codigo '
# Os números acima são os lugares dos seguintes elementos:
# - 1: estilo (negrito/sublinha/negativo)
# - 2: texto (cor do texto)
# - 3: fundo (cor do fundo)

# ESTILO:
# 0 = sem estilo. A fonte será a padrão do terminal
# 1 = negrito. Bordas mais grossas
# 4 = sublinhado. Presença de linha abaixo do texto
# 7 = negativo. Inversão de cores

# TEXTO:
# 30 = branco       # 33 = amarelo      # 36 = ciano
# 31 = vermelho     # 34 = azul         # 37 = cinza
# 32 = verde        # 35 = roxo

# FUNDO:
# 40 = branco       # 43 = amarelo      # 46 = ciano
# 41 = vermelho     # 44 = azul         # 47 = cinza
# 42 = verde        # 45 = roxo

# Exemplo: código em negrito, de cor ciano e fundo cinza:

print('\033[1;36;47mOlá, mundo!\033[m')

# Podemos atribuir cores a diferentes elementos:

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
print(f'A soma entre \033[31m{n1}\033[m e \033[34m{n2}\033[m é igual a \033[35m{soma}\033[m.')