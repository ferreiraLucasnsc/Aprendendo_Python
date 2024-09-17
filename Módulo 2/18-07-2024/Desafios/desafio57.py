# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sexo [M/F]: ')).upper()
while sexo != 'M' and sexo != 'F':
    print('Valor incorreto.')
    sexo = str(input('Informe seu sexo [M/F]: ')).upper()
print('Dado computado.')