# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
# dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

preco = float(input('Digite o preço: R$ '))
import moeda
aum = moeda.aumentar(preco)
dim = moeda.diminuir(preco)
dob = moeda.dobro(preco)
met = moeda.metade(preco)
print('=' * 20)
print('A metade de R$', preco, 'é R$', met)
print('O dobro de R$', preco, 'é R$', dob)
print('Aumentando 10%, temos R$', aum)
print('Diminuindo 10%, temos R$', dim)