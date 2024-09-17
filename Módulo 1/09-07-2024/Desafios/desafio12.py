#       DESAFIO 13

# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

precoOriginal = float(input('Digite o preço do produto: R$ '))
descontoPreco = float(precoOriginal - (precoOriginal * (5/100)))
print(f'O preço do produto, descontado de 5%, é de R$ {descontoPreco}.')