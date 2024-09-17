#       DESAFIO 19

#  Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nomeUser = str(input('Digite seu nome completo: '))
print('ANÁLISE DE NOME:')
print(f'Seu nome maiúsculo: {nomeUser.upper()}\nSeu nome minúsculo: {nomeUser.lower()}')
print(f'Quantas letras seu nome tem: {len(''.join(nomeUser.split()))}')
print(f'Quantas letras seu primeiro nome tem: {len(nomeUser.split()[0])}')