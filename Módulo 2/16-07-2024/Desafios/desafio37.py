# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual
# será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

valorInteiro = int(input('Digite um valor inteiro: '))
print('Escolha qual será a base da conversão:')
print('1 - Binário\n2 - Octal\n3 - Hexadecimal')
baseConversaoEscolha = int(input(': '))
valorConvertido = 0
baseConversaoNome = str
if baseConversaoEscolha == 1:
    valorConvertido = bin(valorInteiro)[2:]
    baseConversaoNome = 'binário'
elif baseConversaoEscolha == 2:
    valorConvertido = oct(valorInteiro)[2:]
    baseConversaoNome = 'octal'
elif baseConversaoEscolha == 3:
    valorConvertido = hex(valorInteiro)[2:]
    baseConversaoNome = 'hexadecimal'
else:
    print('Opção inválida.')
if baseConversaoEscolha < 4:
    print(f'O valor digitado ({valorInteiro}) como um valor {baseConversaoNome} é: {valorConvertido}.')