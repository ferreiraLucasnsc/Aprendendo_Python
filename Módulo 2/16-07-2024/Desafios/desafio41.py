# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

anoNascimento = int(input('Digite o ano de nascimento do atleta: '))
idadeAtleta = int(2024 - anoNascimento)
classificacaoAtleta = str
print('Classificação do atleta: ', end='')
if idadeAtleta > 25:
    classificacaoAtleta = 'MASTER'
elif idadeAtleta > 19:
    classificacaoAtleta = 'SÊNIOR'
elif idadeAtleta > 14:
    classificacaoAtleta = 'JÚNIOR'
elif idadeAtleta > 9:
    classificacaoAtleta = 'INFANTIL'
else:
    classificacaoAtleta = 'MIRIM'
print(classificacaoAtleta)