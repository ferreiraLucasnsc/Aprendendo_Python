# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

print(f'{'\tLEITURA DE GRUPO\t':-^120}')
mais18 = 0
homens = 0
mulheresMenos20 = 0
continuar = ''
while True:
    idade = int(input('Digite a idade da pessoa: '))
    while idade < 0 or idade > 100:
        idade = int(input('Digite uma idade válida: '))
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).upper()
    while sexo not in 'MF':
        sexo = str(input('Digite uma das alternativas [M/F]: ')).upper()
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresMenos20 += 1
    continuar = str(input('Deseja cadastrar mais uma pessoa? [S/N]: ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Digite uma alternativa válida [S/N]> ')).upper()
    if continuar == 'N':
        break
    print('')
print(f'{'-':-^120}')
print('ANÁLISE DE GRUPO:')
print(f'Total de maiores de 18 cadastrados: {mais18}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres menores de 20 cadastradas: {mulheresMenos20}')