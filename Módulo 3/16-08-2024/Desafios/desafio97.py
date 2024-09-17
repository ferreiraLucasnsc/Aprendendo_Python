# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e
# mostre uma mensagem com tamanho adaptável.

def mensagem(txt):
    l = len(txt) + 4
    print('=' * l)
    print(f'{txt:^{l}}')
    print('=' * l)

print('Escreva uma frase, e a exibiremos em uma mensagem adaptável:')
texto = str(input(': '))
print()
mensagem(texto)