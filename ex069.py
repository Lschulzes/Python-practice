maior = homem = mulher_nova = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo : [M/F] ').strip().upper()[0]
    decisao = ' '
    while decisao not in 'SN':
        decisao = input('Quer continuar? [S/N]').strip().upper()
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher_nova += 1
    if decisao == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher_nova} mulheres com menos de 20 anos')
