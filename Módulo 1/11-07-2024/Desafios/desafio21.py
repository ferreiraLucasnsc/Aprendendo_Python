#       DESAFIO 21

# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da sua cidade: '))
primeiroNomeCidade = (cidade.split())[0]
print(f'Sua cidade possui como primeiro nome Santo? {'SANTO' in primeiroNomeCidade.upper()}')