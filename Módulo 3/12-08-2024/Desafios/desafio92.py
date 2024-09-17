# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano
# de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se
# aposentar.

cadastro = dict()
print('     ANÁLISE TRABALHISTA')
print('-'*50)
cadastro['Nome'] = str(input('Nome do trabalhador: '))
cadastro['Ano de Nascimento'] = int(input('Ano de nascimento: '))
cadastro['CTPS'] = int(input('Carteira de trabalho (Caso não tenha, digite 0): '))
if cadastro['CTPS'] != 0:
    cadastro['Ano de Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário do contratado: R$ '))
    cadastro['Aposentadoria'] = (cadastro['Ano de Contratação'] - cadastro['Ano de Nascimento']) + 35
print('='*50)
for k, v in cadastro.items():
    print(f'{k}: {v}')