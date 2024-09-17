# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.

print('='*50)
print(f'{'BOLETIM ESCOLAR':^50}')
print('='*50)
boletim = list()
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    resp = input('Deseja adicionar mais um aluno? [S/N]: ')
    while resp not in 'SsNn':
        print('Resposta inválida')
        resp = input('Deseja adicionar mais um aluno? [S/N]: ')
    if resp in 'Nn':
        break
    print('-'*50)
print('=-'*25)
print(f'{'NÚMERO':<7}{'NOME':<10}{'MÉDIA':>8}')
print('-'*25)
for i, a in enumerate(boletim):
    print(f'{i + 1:<7}{a[0]:<10}{a[2]:>8.1f}')
while True:
    alunoVisto = int(input('De qual aluno deseja ver a nota? (Para parar a vistoria, digite 999): '))
    if alunoVisto <= len(boletim):
        print(f'NOTAS DE {boletim[alunoVisto - 1][0]}:')
        print(f'1ª nota: {boletim[alunoVisto - 1][1][0]}')
        print(f'2ª nota: {boletim[alunoVisto - 1][1][1]}')
    if alunoVisto == 999:
        print('FINALIZANDO PROGRAMA...')
        break
    print('-'*50)