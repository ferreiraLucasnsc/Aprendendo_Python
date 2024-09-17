# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
# dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

cadastro = {}
pessoas = []
soma = media = 0
while True:
    cadastro.clear()
    cadastro['nome'] = str(input('Nome: '))
    cadastro['sexo'] = str(input('Sexo [M/F]: ')).upper()
    while cadastro['sexo'] not in 'MF':
        cadastro['sexo'] = str(input('  Digite uma das alternativas: ')).upper()
    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']
    pessoas.append(cadastro.copy())
    resp = str(input('Deseja continuar? (S/N): ')).upper()
    while resp not in 'SN':
        resp = str(input('  Digite uma das alternativas (S/N): ')).upper()
    if resp in 'Nn':
        break
    print()
print('='*50)
print('     ANÁLISE DOS CADASTROS')
print()
print(f' - Número de pessoas cadastradas: {len(pessoas)}')
media = soma / len(pessoas)
print(f' - Média das idades digitadas: {media:5.2f}')
print(' - Mulheres cadastradas:', end=' ')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p['nome']}', end=' / ')
print()
print('- Pessoas com idade acima da média:')
for p in pessoas:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}', end='   ')