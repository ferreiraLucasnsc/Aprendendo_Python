#       DESAFIO 22

# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nomeCompleto = str(input('Digite seu nome completo: ')).strip()
divisao = nomeCompleto.upper().split()
print(f'Seu nome possui a palavra Silva? {'SILVA' in divisao}')