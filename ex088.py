from random import randint
from time import sleep


jogo = list()
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 5, f' SORTEANDO {quantidade} JOGOS ', '-=' * 5)
for i in range(1, quantidade + 1):
    c = 1
    while c < 7:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            c += 1
    jogo.sort()
    print(f'Jogo {i}: {jogo}')
    sleep(0.5)
    jogo.clear()
print('-=' * 5, ' < BOA SORTE! > ', '-=' * 5)
