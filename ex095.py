dicio = {}
total = 0
gols = []
time = list()

continuar = ' '
while continuar not in 'SN':
    dicio['nome'] = input('Nome do jogador: ').strip().capitalize()
    partidas = int(input(f'Quantas partidas {dicio["nome"]} jogou? '))
    for games in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols na partida {games}? ')))
        total += gols[games - 1]
    dicio['gols'] = gols[:]
    dicio['total'] = total
    gols.clear()
    time.append(dicio.copy())
    total = 0
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
    continuar = ' '
print('-=' * 30)
print('cod ', end='')
for i in dicio.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>4}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
while True:
    cod = int(input('Mostrar os dados de qual jogador (999 para sair)? '))
    if cod == 999:
        break
    if cod >= len(time):
        print(f'ERRO! Não existe um jogador com o código {cod}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[cod]["nome"]}:')
        for k, b in enumerate(time[cod]['gols']):
            print(f'No jogo {k + 1} fez {b} gols.')
    print('-' * 40)
print('<<<VOLTE SEMPRE>>>')
