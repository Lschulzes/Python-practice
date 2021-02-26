velocidade = int(input("Digite quantos Km/h o carro estava: "))
multa = 0
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'A multa foi no valor de {multa} reais!')
else:
    print('Tenha um bom dia e dirija com segurança!')
