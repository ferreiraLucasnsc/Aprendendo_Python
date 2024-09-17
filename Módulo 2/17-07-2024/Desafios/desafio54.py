# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
menores = 0
for c in range (0, 7):
    anoNascimento = int(input(f'Digite o ano em que a {c+1}ª pessoa nasceu: '))
    if date.today().year - anoNascimento < 18:
        menores += 1
print(f'Destas sete pessoas, {menores} são menores de idade, enquanto {7 - menores} são maiores de idade.')