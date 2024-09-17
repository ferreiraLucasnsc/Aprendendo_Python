#       DESAFIO 13

# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salarioOriginal = float(input('Digite o salário do funcionário: R$ '))
salarioAumento = float(salarioOriginal + (salarioOriginal * (15/100)))
print(f'O novo salário do funcionário, acrescido de 15%, é de R$ {salarioAumento}.')