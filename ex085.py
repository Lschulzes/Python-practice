valores = [[], []]
for i in range(1, 8):
    num = int(input(f'Digite o {i}º. valor: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
valores[0].sort()
valores[1].sort()
print(f'Ímpares : {valores[1]}')
print(f'Pares : {valores[0]}')
