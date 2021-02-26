from random import randint
from time import sleep
from operator import itemgetter


game = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
rank = []
print('Valores sorteados:')
for k, v in game.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
rank = sorted(game.items(), key=itemgetter(1), reverse=True)
print('-=' * 20)
print('       == RANKING DOS JOGADORES ==')
for k, v in enumerate(rank):
    print(f'{k + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
