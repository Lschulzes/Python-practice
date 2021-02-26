altura = float(input('Qual a sua altura em metros? '))
peso = int(input('Qual o seu peso em quilogramas? '))
bmi = peso / (altura * altura)
if bmi < 18.5:
    print(f'Você está abaixo do peso com um IMC de {bmi}')
elif bmi < 25:
    print(f'Você está com um peso ideal e um IMC de {bmi}')
elif bmi < 30:
    print(f'Você está com sobrepeso e um IMC de {bmi}')
elif bmi < 40:
    print(f'Você está obeso e com um IMC de {bmi}')
else:
    print(f'Você está com obesidade mórbida e um IMC de {bmi}')
