# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
# o empréstimo será negado.

valorCasa = float(input('Qual é o valor da casa desejada? R$ '))
salarioComprador = float(input('Qual é o seu salário? R$ '))
anosCompra = int(input('Em quantos anos deseja pagar o empréstimo? '))
prestacaoMensal = valorCasa / (anosCompra * 12)
minimoPermitido = salarioComprador * 30 / 100
print(f'Para pagar uma casa de R$ {valorCasa:.2f} em {anosCompra} anos, será feito uma', end=' ')
print(f'prestação de R$ {prestacaoMensal:.2f}.')
print(f'Sendo que o mínimo permitido de prestações é de R$ {minimoPermitido:.2f}, seu empréstimo', end=' ')
if prestacaoMensal > minimoPermitido:
    print(f'é maior que o permitido. Empréstimo negado.')
else:
    print(f'está dentro do permitido. Empréstimo concedido.')