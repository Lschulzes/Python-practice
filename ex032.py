ano = int(input('Qual o ano em que você está? '))


if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
