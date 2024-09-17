#       DESAFIO 24

# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o 
# último nome separadamente.

nomeCompleto = str(input('Digite seu nome completo: ')).title()
nomeDivisao = nomeCompleto.split()
print(f'O seu primeiro nome é {nomeDivisao[0]}, e seu último nome é {nomeDivisao[len(nomeDivisao) - 1]}')