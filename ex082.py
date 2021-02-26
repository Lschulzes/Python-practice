todos = []
pares = []
impares = []
while True:
    todos.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Você deseja continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
for a in range(0, len(todos)):
    if todos[a] % 2 == 0:
        pares.append(todos[a])
    else:
        impares.append(todos[a])
print(f'''A lista de todos os valores digitados: {todos}
Números pares: {pares}
Números ímpares: {impares}''')
