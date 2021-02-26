sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Qual o seu sexo? [M/F] ').strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Não consegui reconhecer seu sexo, tente novamente!')
