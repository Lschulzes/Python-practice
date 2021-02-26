todos = []
c = 1
for a in range(0, 5):
    valor = int(input('Digite um valor: '))
    todos.append(valor)
    while True:
        if valor < todos[a - c]:
            c += 1
        else:
            todos.insert(a - c + 1, valor)
            del todos[a + 1]
            if c == 1:
                print(f'Valor [{valor}] adicionado ao final da lista...')
                c = 1
                break
            else:
                print(
                    f'Valor [{valor}] adicionado na posição [{a - c + 1}] da lista...')
                c = 1
                break
print(todos)
