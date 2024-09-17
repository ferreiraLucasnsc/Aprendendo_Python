# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

estoque = ('Lápis', 1.75,
           'Borracha', 2.00,
           'Caderno', 15.90,
           'Estojo', 25.00,
           'Transferidor', 4.20,
           'Compasso', 9.99,
           'Mochila', 120.32,
           'Canetas', 22.30,
           'Livro', 34.90)
print(f'{' LISTAGEM DE PREÇOS ':=^50}')
for item in estoque:
    if type(item) == str:
        print(f'{item:.<43}', end='')
    else:
        print(f'R$ {item:<5.2f}')