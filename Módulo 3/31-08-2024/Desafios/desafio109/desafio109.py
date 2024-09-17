# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.

preco = float(input('Digite o preço: R$ '))
import moeda
while True:
    formatarStr = str(input('Deseja ver os resultados formatados? [S/N]: '))
    if formatarStr in 'Ss':
        formatarBool = True
    else:
        formatarBool = False
    if formatarStr not in 'SsNn':
        print(' DIGITE UM VALOR VÁLIDO')
    else:
        break
print('=' * 20)
print('A metade de', moeda.moeda(preco), 'é', moeda.metade(preco, formatarBool))
print('O dobro de', moeda.moeda(preco), 'é', moeda.dobro(preco, formatarBool))
print('Aumentando 10%, temos', moeda.aumentar(preco, 10, formatarBool))
print('Diminuindo 13%, temos', moeda.diminuir(preco, 13, formatarBool))