dados = list()
momento = list()
continuar = ' '
while continuar != 'N':
    momento.append(input('Nome: '))
    momento.append(int(input('Peso: ')))
    dados.append(momento[:])
    momento.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Você deseja continuar? [S/N] ').strip().upper()
        if continuar == 'N':
            break
maior = menor = 0
for i in dados:
    if i[1] >= maior:
        maior = i[1]
    elif i[1] <= menor or menor == 0:
        menor = i[1]
cadastros = len(dados)
print('-=' * 40)
print(f'Ao todo você realizou {cadastros} cadastros')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for i in dados:
    if i[1] == maior:
        print(f'[{i[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for i in dados:
    if i[1] == menor:
        print(f'[{i[0]}]', end=' ')
