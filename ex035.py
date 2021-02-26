reta_1 = float(input('Quantos centímetros a reta 1 tem? '))
reta_2 = float(input('Quantos centímetros a reta 2 tem? '))
reta_3 = float(input('Quantos centímetros a reta 3 tem? '))
maior = 0
menores = 0
if reta_1 > reta_2:
    if reta_1 > reta_3:
        maior = reta_1
        menores = reta_2 + reta_3
    else:
        maior = reta_3
        menores = reta_1 + reta_2
elif reta_2 > reta_3:
    maior = reta_2
    menores = reta_1 + reta_3
else:
    maior = reta_3
    menores = reta_1 + reta_2
if menores > maior:
    print('É possível formar um triângulo com essas retas!')
else:
    print('Não é possível formar um triângulo com essas retas!')
