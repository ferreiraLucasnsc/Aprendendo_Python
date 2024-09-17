# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

print(f'{' TABUADA ':-^120}')
print('Digite um número, e calcularei a tabuada dele para você')
print('Caso deseja parar a criação de tabuadas, basta digitar um número negativo')
multiplica = 0
resultado = 0
while True:
    numero = int(input('Número para tabuada: '))
    if numero < 0:
        print(f'{'-':-^120}')
        print('Programa encerrado')
        break
    for multiplica in range (1, 11):
        resultado = multiplica * numero
        print(f'{numero} x {multiplica} = {resultado}')
    multiplica = 0
    resultado = 0
    print(f'{'-':-^120}')
print('Fim do cálculo de tabuadas')