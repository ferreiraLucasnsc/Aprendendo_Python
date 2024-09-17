#       DESAFIO 04

# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo
# e todas as informações possíveis sobre ele.

valor = input('Digite alguma coisa: ')
print('     ANÁLISE DO VALOR:')
print('Tipo primitivo: {}\nO valor digitado é um:'.format(type(valor)))
print('     Número? {}\n     Letra? {}\n'.format(valor.isnumeric(), valor.isalpha()))
print('É maiúsculo? {}\nÉ minúsculo? {}.'.format(valor.isupper(), valor.islower()))
print('É um espaço vazio? {}'.format(valor.isspace()))

# print(f'Teste: o valor digitado foi {valor}'): nova sintaxe de impressão de variáveis