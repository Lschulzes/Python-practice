tudo = list()
momento = [[], []]
n = 0
contiuar = ' '
while contiuar != 'N':
    momento[0].append(input('Nome: ').strip().capitalize())
    momento[1].append(float(input('Nota 1: ')))
    momento[1].append(float(input('Nota 2: ')))
    tudo.append(momento[:])
    momento = [[], []]
    n += 1
    contiuar = ' '
    while contiuar not in 'SN':
        contiuar = input('Deseja continuar? [S/N]: ').strip().upper()
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for i in range(0, n):
    media = (tudo[i][1][0] + tudo[i][1][1]) / 2
    print(f'{i:<4}{tudo[i][0][0]:<10}{media:>8.2f}')
print('-' * 30)
while True:
    aluno = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        break
    print(f'Notas de {tudo[aluno][0][0]} são {tudo[aluno][1]}')
