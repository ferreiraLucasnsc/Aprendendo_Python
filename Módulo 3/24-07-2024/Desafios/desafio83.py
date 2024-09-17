# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e
# fechados na ordem correta.

print(f'{' ANALISADOR DE EXPRESSÕES ':-^50}')
exp = str(input('Digite aqui sua expressão: '))
pilha = []
for char in exp:
    if char == '(':
        pilha.append(char)
    elif char == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Tudo certo! Sua expressão está correta!')
else:
    print('Opa! Sua expressão está errada! Verifique a abertura dos parênteses...')