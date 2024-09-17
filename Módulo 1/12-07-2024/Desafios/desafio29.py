#       DESAFIO 29

# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
print('\t\t\t\tANO BISSEXTO')
print('='*100)
print('Digite um ano, e analisarei se este é bissexto. Digite 0 para ver o ano atual.')
ano = int(input(': '))
if (ano == 0):
    ano = date.today().year

if (ano % 4 == 0 and ano % 100 != 0):
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} é comum.')
print('='*100)