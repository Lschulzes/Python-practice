lista = [[[], [], []], [[], [], []], [[], [], []]]
for i in range(0, 3):
    for j in range(0, 3):
        lista[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{lista[i][j]}]', end='')
    print()
soma_par = soma_ter = maior = 0
for i in range(0, 3):
    soma_ter += lista[i][j]
    for j in range(0, 3):
        if lista[i][j] % 2 == 0:
            soma_par += lista[i][j]
        if lista[1][j]:
            if lista[1][j] > maior:
                maior = lista[1][j]
print(f'''A soma dos valores pares é {soma_par}
A soma dos valores da terceira coluna é {soma_ter}
O maior valor da segunda linha é {maior}''')
