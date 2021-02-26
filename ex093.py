dicio = {}
total = 0
gols = []

dicio['nome'] = input('Nome do jogador: ').strip().capitalize()
partidas = int(input(f'Quantas partidas {dicio["nome"]} jogou? '))
for games in range(1, partidas + 1):
    gols.append(int(input(f'Quantos gols na partida {games}? ')))
    total += gols[games - 1]
dicio['gols'] = gols
dicio['total'] = total
print('-=' * 40)
for b, v in dicio.items():
    print(f'O campo {b} tem o valor {v}.')
print('-=' * 40)
z = 0
while z == 0:
    for z in dicio.values():
        print(f'O jogador {z} jogou {partidas} partidas.')
for jogos in range(1, partidas + 1):
    print(f'      => Na partida {jogos}, fez {gols[jogos - 1]}')
print(f'Foi um total de {total} gols.')
