while True:
    info = {}
    info['nome'] = input('Nome: ')
    info['idade'] = 2021 - int(input('Ano de Nascimento: '))
    info['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    if info['ctps'] == 0:
        break
    info['contratação'] = int(input('Ano da 1ª contratação: '))
    info['salario'] = int(input('Salário: R$'))
    info['aposentadoria'] = info['contratação'] - 2021 + info['idade'] + 35
    break
print('-=' * 50)
for i, v in enumerate(info.items()):
    print(f'{v[0]} tem o valor {v[1]}')
