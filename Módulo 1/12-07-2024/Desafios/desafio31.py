#       DESAFIO 31

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
# o aumento é de 15%.

print('\t\t\t\tAUMENTO SALARIAL')
print('*'*100)
salario = float(input('Digite o salário do funcionário: R$ '))
aumento = 0
if salario > 1250.00:
    aumento = 10/100
else:
    aumento = 15/100
novoSalario = salario + (salario * aumento)
print(f'O novo salário do funcionário é de R$ {novoSalario}.')
print('*'*100)