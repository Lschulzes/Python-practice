valores = []
quanti = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    quanti += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
valores.sort(reverse=True)
print(f'''Você digitou {quanti} elementos.
Os valores em ordem decrescente são {valores}''')
if 5 not in valores:
    print('O valor 5 não foi encontrado na lista!')
else:
    print('O valor 5 faz parte da lista!')
