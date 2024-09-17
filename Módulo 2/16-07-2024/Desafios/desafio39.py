# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
# do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

anoJovem = int(input('Digite o ano de seu nascimento: '))
idadeJovem = int(2024 - anoJovem)
print(f'Se você nasceu em {anoJovem}, você tem/fará {idadeJovem} anos em 2024.')
if idadeJovem == 18:
    print('Está na hora do seu alistamento.')
elif idadeJovem < 18:
    print('Ainda não está na hora do seu alistamento.')
    if 18 - idadeJovem == 1:
        print(f'Falta 1 ano para o seu alistamento.')
    else:
        print(f'Faltam {18 - idadeJovem} anos para o seu alistamento.')
else:
    print('Já passou da hora do seu alistamento.')
    if idadeJovem - 18 == 1:
        print('Se passou 1 ano do seu alistamento.')
    else:
        print(f'Se passaram {idadeJovem - 18} anos do seu alistamento.')