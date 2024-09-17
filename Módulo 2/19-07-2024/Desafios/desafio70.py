# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('\t\t\t\tCADASTRO DE COMPRAS')
print('=' * 130)
totalGasto = produtosMais1000 = 0
maisBaratoNome = continuar = ''
maisBaratoPreco = 0
c = 0
while True:
    nomeProduto = str(input('Digite o nome do produto: '))
    precoProduto = float(input('Digite o preço do produto: R$ '))
    c += 1
    while precoProduto <= 0:
        precoProduto = float(input('Digite o preço adequado: R$ '))
    totalGasto += precoProduto
    if precoProduto > 1000:
        produtosMais1000 += 1
    if c == 1:
        maisBaratoPreco = precoProduto
        maisBaratoNome = nomeProduto
    else:
        if precoProduto < maisBaratoPreco:
            maisBaratoPreco = precoProduto
            maisBaratoNome = nomeProduto
    continuar = str(input('Deseja adicionar mais um produto? [S/N]: ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Digite uma das alternativas [S/N]: '))
    if continuar == 'N':
        break
    print('')
print('ANÁLISE DOS PRODUTOS:')
print(f'Total gasto: R$ {totalGasto}\nProdutos mais de R$ 1000: {produtosMais1000}\nProduto mais barato: {maisBaratoNome} (Preço R$ {maisBaratoPreco})')