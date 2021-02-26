lista = [[[], [], []], [[], [], []], [[], [], []]]
for i in range(0, 3):
    for j in range(0, 3):
        lista[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{lista[i][j]}]', end='')
    print()
