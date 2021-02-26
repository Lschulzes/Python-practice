express = input('Digite a expressão: ')
pilha = []
for letra in express:
    if letra == '(':
        pilha.append('(')
    elif letra == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append('errou')
            break

if len(pilha) == 0:
    print('A expressão está válida!')
else:
    print('A expressão está errada!')
