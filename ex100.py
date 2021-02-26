from time import sleep
from random import randint


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        num = randint(0, 10)
        lista.append(num)
        print(f'{num}', end='-> ', flush=True)
        sleep(0.5)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}', end='')


numeros = list()
sorteia(numeros)
somapar(numeros)
