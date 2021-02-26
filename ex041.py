ano = int(input('Digite o ano do seu nascimento: '))
idade = 2021 - ano
if idade < 9:
    print('O atleta se encontra na categoria mirim.')
elif idade < 14:
    print('O atleta se encontra na categoria infantil.')
elif idade < 19:
    print('O atleta se encontra na categoria junior.')
elif idade < 20:
    print('O atleta se encontra na categoria sênior.')
else:
    print('O atleta se encontra na categoria master.')
