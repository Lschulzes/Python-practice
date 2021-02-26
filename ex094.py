pessoa = {}
grupo = []
soma = 0
continuar = ' '
while continuar != 'N':
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo: [M/F] ').strip().upper()
    pessoa['idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())
    soma += pessoa['idade']
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
        if continuar == 'N':
            break
print('-=' * 40)
quantidade = len(grupo)
media = soma / quantidade
print(f'- O grupo tem {quantidade} pessoas.')
print(f'- A média de idade é de {media:5.2f} anos')
print(f'- As mulheres cadastradas foram ', end='')
for p in grupo:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'- Lista das pessoas que estão acima da média:')
for p in grupo:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<<<<ENCERRADO>>>>')
