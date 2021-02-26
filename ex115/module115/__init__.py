import os
from time import sleep


def optionmenu(msg):
    print('-' * 50)
    print(msg.center(50))
    print('-' * 50)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova Pessoa')
    print('3 - Sair do sistema')
    print('-' * 50)
    opt = int(input('Sua opção: '))
    return opt


def showlist(msg, listname):
    print('-' * 50)
    print(msg.center(50))
    print('-' * 50)
    texto = open(listname, 'rt')
    for linha in texto:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        print(f'{dado[0]}{dado[1]}')
    print('-' * 50)
    texto.close()
    sleep(1.75)


def optionsair(msg):
    print('-' * 50)
    print(msg.center(50))
    print('-' * 50)
    sleep(3)


def writelistname(msg, listname):
    while True:
        n = str(input(msg)).strip().capitalize()
        if n.isnumeric():
            print('Entrada inválida, não é permitido números!')
        elif n == '':
            print('Digite um nome!')
        else:
            n = (f'{n:<40};')
            texto = open(listname, 'a+')
            texto.write(n)
            texto.close()
            break


def writelistage(msg, listname):
    while True:
        n = str(input(msg)).strip().upper()
        if n.isupper():
            print('Entrada inválida, não é permitido letras!')
        elif n == '':
            print('Digite uma idade!')
        else:
            n = (f'{n:>3} anos.\n')
            texto = open(listname, 'a+')
            texto.write(n)
            texto.close()
            break
