distancia = int(input('Qual a distância da sua viagem? '))
preço = 0
if distancia < 200:
    preço = 0.5 * distancia
    print(f'O preço da viagem é de R${preço:.2f}!')
else:
    preço = 0.45 * distancia
    print(f'O preço da viagem é de R${preço:.2f}!')
