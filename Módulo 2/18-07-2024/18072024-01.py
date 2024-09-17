#       LAÇOS DE REPETIÇÃO - 2

# Vimos a estrutura FOR, que nos permite repetir o teste de uma condição por um tempo de iterações fixo.
# Existem caso, porém, em que este número nem sempre será fixo. Pode ser de acordo com uma ação do usuário, uma variável que
# não sabemos quando será concluída, entre outros casos.

# Para estes casos, temos a estrutura WHILE.

# A estrutura WHILE repete um código enquanto uma determinada condição é verdadeira. Quando esta deixa de ser, o código sai da
# estrutura de repetição e continua seu fluxo.
# Como nesta estrutura não temos uma atualização dentro da sintaxe padrão, temos de criar uma linha para o incremento da variável
# de controle, ou nosso laço se torna um loop infinito.

# Esta e a sintaxe da estrutura WHILE:

# while condição:
#   ...

# Seu fluxo é bem parecido com a estrutura FOR. Afinal, ambas são estruturas de repetição:

# WHILE condicao    ->  codigo2 ->  FIM     =>  caso false
#      |                             ^
#      V                             |
# codigo1           =>               o      =>  caso true

# Vamos usar o primeiro exemplo de repetição (lançamento), desta vez com a estrutura WHILE:

print('Contagem regressiva para o lançamento!')
contagem = 10
while contagem > 0:
    print(f'{contagem}...')
    contagem -= 1
print('Lançamento concluído!')

# Perceba: testamos a condição da contagem ser maior que 0, o que inicia verdadeiro. Se não mudarmos o valor da contagem, esta
# condição sempre será verdadeira. Então, acresentamos a linha de atualização da variável: no caso, um decremento de 1.
# Ao chegar no valor 0, a contagem NÂO será maior do que 0. Sendo falsa a condição, o código segue o fluxo normal, terminando a
# estrutura de repetição.

# A parte que o WHILE realmente brilha é na entrada de valores de parada:

print('SOMA DE VALORES')
print('Para parar a soma, aperte o número 0.')
soma = 0
valor = 1
while (valor != 0):
    valor = int(input('Digite um valor: '))
    soma += valor
print('Ao final dos números digitados, a soma é igual a', soma)

# Aqui, temos que o laço para só quando o valor digitado for 0. Ao contrário do laço acima, agora a responsabilidade de parada está
# nas mãos do USUÁRIO: só quando ele digitar o valor de parada que o laço irá ser interrompido.