# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e
# quantas mulheres têm menos de 20 anos.

media = 0
maiorIdade = 0
mulheresMenos20 = 0
maisVelho = ''
somaIdade = 0
for c in range(1, 4+1):
    nome = str(input(f'Digite o nome da {c}ª pessoa: '))
    idade = int(input(f'Digite a idade da {c}ª pessoa: '))
    print(f'Digite o sexo da {c}ª pessoa:')
    print('[1] Masculino\n[2] Feminino\n[3] Outra opção')
    sexo = int(input(': '))
    somaIdade += idade
    if c == 0:
        idade = maiorIdade
    else:
        if sexo == 1 and idade > maiorIdade:
            maisVelho = nome
        if sexo == 2 and idade < 20:
            mulheresMenos20 += 1
media = somaIdade / 4
print(f'A média das idades do grupo é de {media} anos.')
print(f'O nome do homem mais velho é {maisVelho}.')
if mulheresMenos20 == 0:
    print('Não foram computadas mulheres com menos de 20 anos.')
elif mulheresMenos20 == 1:
    print('Foi computada somente uma mulher com menos de 20 anos.')
else:
    print(f'Foram computadas {mulheresMenos20} mulheres com menos de 20 anos.')