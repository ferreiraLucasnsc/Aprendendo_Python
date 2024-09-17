# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

numero = int(input('Digite o número para sua tabuada ser calculada: '))
print(f'\n\t\t\t\tTABUADA DE {numero}')
multiplicacao = 0
resultado = 0
for multiplicacao in range (0, 10+1):
    resultado = numero * multiplicacao
    print(f'{numero}\tX\t{multiplicacao}\t=\t{resultado}')