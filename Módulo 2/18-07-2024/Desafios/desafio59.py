#  Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

print('\t\tCALCULADORA')
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
escolha = 0
while escolha != 5:
    print('\t\tMENU DE OPÇÕES')
    print('[1] Soma\n[2] Multiplicação\n[3] Comparação\n[4] Novos números\n[5] Fechar programa')
    escolha = int(input('Qual opção você deseja? '))
    while escolha > 5 or escolha < 1:
        escolha = int(input('Esta opção não está entre as selecionáveis. Digite novamente: '))
    print('\t\t', '-' * 50)
    if escolha == 1:
        print(f'A soma entre {valor1} e {valor2} é {valor1 + valor2}')
    elif escolha == 2:
        print(f'A multiplicação de {valor1} por {valor2} é igual a {valor1 * valor2}')
    elif escolha == 3:
        if valor1 > valor2:
            print('O primeiro valor é maior')
        elif valor1 < valor2:
            print('O segundo valor é maior')
        else:
            print('Ambos valores são iguais')
    elif escolha == 4:
        print('Insira os novos valores')
        valor1 = float(input('Digite o primeiro valor: '))
        valor2 = float(input('Digite o segundo valor: '))
    else:
        print('Finalizando programa...')
    print('-' * 100)