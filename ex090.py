situa = dict()
situa['nome'] = input('Nome: ')
situa['media'] = float(input(f'Média de {situa["nome"]}: '))
if situa['media'] >= 7:
    situa['situação'] = 'Aprovado'
else:
    situa['situação'] = 'Reprovado'
for k, v in situa.items():
    print(f'{k} é igual a {v}')
