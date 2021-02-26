menor = caros = soma = 0


while True:
    nome = input('Nome do produto: ').strip()
    preco = int(input('Preço: '))
    soma += preco
    if preco < menor or menor == 0:
        nome_menor = nome
        menor = preco
    if preco > 1000:
        caros += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
print(f'''O total da compra for de R${soma}
Temos {caros} produtos custando mais de R$1000.00
O produto mais barato foi {nome_menor} que custa R${menor}''')
