ano = int(input('Qual o ano do seu nascimento? '))
idade = 2021 - ano
passou = idade - 18
falta = 18 - idade
if idade == 18:
    print('Você deve se alistar neste ano!')
elif idade > 18:
    print(f'Você deveria ter se alistado há {passou} anos!')
else:
    print(f'Você deverá se alistar em {falta} anos!')
