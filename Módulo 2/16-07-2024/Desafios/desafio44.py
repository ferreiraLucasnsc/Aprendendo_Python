# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

precoProduto = float(input('Digite o preço do produto a ser comprado: R$ '))
print('Veja as opções de pagamento:')
print('[1] À vista:', '10%', 'de desconto')
print('[2] À vista no cartão:', '5%', 'de desconto')
print('[3] Até 2x no cartão: preço formal')
print('[4] Até 3x ou mais no cartão:', '20%', 'de juros')
opcaoPagar = int(input('Qual será a forma de pagamento? '))
adicional = 0
if opcaoPagar == 1:
    adicional = 10/100
elif opcaoPagar == 2:
    adicional = 5/100
elif opcaoPagar == 3:
    adicional = 0
else:
    adicional = 20/100
if adicional > 0:
    if opcaoPagar == 4:
        novoPreco = precoProduto + (precoProduto * adicional)
    else:
        novoPreco = precoProduto - (precoProduto * adicional)

print(f'A partir da forma de pagamento, o valor do produto é de R$ {novoPreco}')