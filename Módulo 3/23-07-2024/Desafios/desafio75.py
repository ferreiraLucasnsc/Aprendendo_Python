# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

valores = tuple(int(input('Digite um valor: ')) for i in range(4))
if 9 not in valores:
    print('* O número 9 não foi digitado')
else:
    print('* O número 9 foi digitado', valores.count(9), 'vezes')
if 3 in valores:
    print('* O primeiro 3 foi digitado na posição', valores.index(3))
else:
    print('* Não foi digitado o número 3')
print('* Os valores pares digitados foram:', end=' ')
for n in valores:
    if n % 2 == 0:
        print(n, end='  ')