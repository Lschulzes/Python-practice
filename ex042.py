reta_1 = float(input('Quantos centímetros a reta 1 tem? '))
reta_2 = float(input('Quantos centímetros a reta 2 tem? '))
reta_3 = float(input('Quantos centímetros a reta 3 tem? '))
if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print('É possível formar um triângulo com essas retas!')
else:
    print('Não é possível formar um triângulo com essas retas!')
if reta_1 == reta_2 == reta_3:
    print('Este triângulo é equilátero!')
elif reta_1 == reta_2 or reta_1 == reta_3 or reta_2 == reta_3:
    print('Este triângulo é isóceles!')
else:
    print('Este triângulo é escaleno!')
