# Adapte o código do desafio #107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.

preco = float(input('Digite o preço: R$ '))
import moeda
aum = moeda.aumentar(preco)
dim = moeda.diminuir(preco)
dob = moeda.dobro(preco)
met = moeda.metade(preco)
print('=' * 20)
print('A metade de R$', moeda.moeda(preco), 'é R$', moeda.moeda(met))
print('O dobro de R$', moeda.moeda(preco), 'é R$', moeda.moeda(dob))
print('Aumentando 10%, temos R$', moeda.moeda(aum))
print('Diminuindo 10%, temos R$', moeda.moeda(dim))