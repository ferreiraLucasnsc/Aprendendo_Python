#       DESAFIO 23

# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que 
# posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
letra = str('A')
print(f'A letra {letra} aparece {frase.count(letra)} vezes.')
print(f'A primeira letra {letra} aparece na {(frase.find(letra)) + 1}ª posição.')
print(f'A última letra {letra} aparece na {(frase.rfind(letra)) + 1}ª posição.')