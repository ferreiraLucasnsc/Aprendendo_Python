# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
# um dicionário com as seguintes informações:

# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)

# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def analiseNotas(n, s='N'):
    '''
    --> Realiza uma análise das notas enviadas e retorna um dicionário com os resultados
    Parâmetros:
        - n: notas no formato de uma lista
        - s: situação dos alunos, podendo ser exibida ou não
    O retorno consiste de um dicionário detalhado, contendo as seguintes informações:
        - Quantidade de notas registradas
        - Maior e menor nota
        - Média das notas registradas
        - Situação dos alunos (opcional)
    '''
    analise = dict()
    analise['quantidade'] = len(n)
    analise['maior'] = max(n)
    analise['menor'] = min(n)
    c = 0
    soma = 0
    while c < len(n):
        soma += n[c]
        c += 1
    analise['media'] = soma / len(n)
    if s == 'S':
        if analise['media'] >= 7:
            analise['situacao'] = 'BOA'
        elif analise['media'] >= 5:
            analise['situacao'] = 'RAZOÁVEL'
        else:
            analise['situacao'] = 'RUIM'
    return analise

notas = list()
while True:
    nota = float(input('Digite a nota do aluno: '))
    notas.append(nota)
    resp = input('Deseja adicionar mais notas? [S/N]: ')
    while resp not in 'SsNn':
        resp = input('  Digite uma das alternativas [S/N]: ')
    if resp in 'Nn':
        print('Fim da adição de notas')
        break
    print('-' * 50)
print('-' * 50)
situ = str(input('Deseja ver a situação da turma? [S/N]: ')).upper()
while situ not in 'SsNn':
    situ = str(input('  Digite uma das alternativas [S/N]: ')).upper()
print()
a = analiseNotas(notas, situ)
print(f'{' ANÁLISE DA TURMA':=^50}')
print(f'Quantidade de notas registradas: {a['quantidade']:>17}')
print(f'Maior nota registrada: {a['maior']:>27}')
print(f'Menor nota registrada: {a['menor']:>27}')
print(f'Média das notas registradas: {a['media']:>21.2f}')
if situ == 'S':
    frase = f'Situação da turma: {a['situacao']}'
    print(f'{frase:^50}')
resp = input('Deseja ver a docstring da função de análise? [S/N]: ').upper()
if resp == 'S':
    help(analiseNotas)