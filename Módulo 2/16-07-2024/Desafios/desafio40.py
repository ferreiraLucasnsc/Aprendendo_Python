# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = float((nota1 + nota2) / 2.0)
if media >= 7.0:
    print('Aluno aprovado.')
elif media >= 5.0:
    print('Aluno em recuperação.')
else:
    print('Aluno reprovado.')