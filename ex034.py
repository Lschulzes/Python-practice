sal = int(input('Qual o seu salário atual? '))

if sal > 1250:
    novo_sal = sal * 1.1
    print(f'Seu novo salário é de R${novo_sal}')
else:
    novo_sal = sal * 1.15
    print(f'Seu novo salário é de R${novo_sal}')
