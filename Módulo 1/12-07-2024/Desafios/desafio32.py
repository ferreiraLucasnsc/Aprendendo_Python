#       DESAFIO 32

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
# formar um triângulo.

print('\t\t\t\tANALISADOR DE TRIÂNGULOS')
print('=' * 100)
print('Digite a medida de três retas, e direi se elas podem formar um triângulo.')
reta1 = float(input('Reta 1: '))
reta2 = float(input('Reta 2: '))
reta3 = float(input('Reta 3: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Estas três retas podem formar um triângulo.')
else:
    print('Estas três retas não podem formar um triângulo.')
print('=' * 100)