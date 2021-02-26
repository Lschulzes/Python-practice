valores = []

while True:
    valor = (int(input('Digite um valor: ')))
    if valor in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
print('-=' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')
