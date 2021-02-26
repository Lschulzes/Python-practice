valor = int(input('Qual valor você quer sacar? R$'))
cd50 = cd20 = cd10 = cd1 = 0
while True:
    if valor >= 50:
        cd50 += 1
        valor -= 50
    elif valor >= 20:
        cd20 += 1
        valor -= 20
    elif valor >= 10:
        cd10 += 1
        valor -= 10
    elif valor >= 1:
        cd1 += 1
        valor -= 1
    else:
        break
print(f'''Total de {cd50} cédulas de R$50
Total de {cd20} cédulas de R$20
Total de {cd10} cédulas de R$10
Total de {cd1} cédulas de R$1''')
