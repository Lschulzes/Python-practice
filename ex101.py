def voto(idade):
    print(f'Com {idade} anos: ', end='')
    if idade >= 18 and idade <= 70:
        print(f'Voto obrigatório')
    elif idade < 18 and idade >= 16 or idade > 70:
        print(f'Voto opcional.')
    else:
        print(f'Não pode votar ainda.')


print('-' * 40)
i = 2021 - int(input('Em que ano você nasceu? '))
voto(i)
