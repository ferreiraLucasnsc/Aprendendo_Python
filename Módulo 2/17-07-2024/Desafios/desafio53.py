# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA.

texto = (str(input('Digite uma palavra/frase, e direi se ela é um palíndromo: ')).upper()).strip()
palavras = texto.split()
textoBase = ''.join(palavras)
textoInverso = ''
for letra in range(len(textoBase) - 1, -1, -1):
    textoInverso += textoBase[letra]
print(f'O texto {texto} ao contrário é {textoInverso}.')
if textoInverso == textoBase:
    print('Como ambos são iguais, seu texto é palíndromo.')
else:
    print('Como são diferentes, seu texto não é palíndromo.')