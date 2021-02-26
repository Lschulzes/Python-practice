import random
from time import sleep

print('Bem-vindo a sala de Jokenpô! O primeiro que vencer 3 vezes ganha!')
print('''1 - pedra
2 - papel
3 - tesoura''')
humano = 0
pc = 0
while humano < 3 and pc < 3:
    escolha = int(input('Pedra, papel, tesouuura: '))
    maquina = random.randint(1, 3)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!')
    print('-=' * 20)
    if escolha > 3:
        print('Fuk youu, play by the rules!')
    elif escolha == maquina:
        print('Empate!')
    elif escolha == 1:
        if maquina == 2:
            print('O adversário jogou papel, você perdeu!')
            pc += 1
        else:
            print('O adversário jogou tesoura, você ganhou!')
            humano += 1
    elif escolha == 2:
        if maquina == 1:
            print('O adversário jogou pedra, você ganhou!')
            humano += 1
        else:
            print('O adversário jogou tesoura, você perdeu!')
            pc += 1
    else:
        if maquina == 1:
            print('O adversário jogou pedra, você perdeu!')
            pc += 1
        else:
            print('O adversário jogou papel, você ganhou!')
            humano += 1
    print('-=' * 20)
if humano < pc:
    print(f'Você perdeu de {humano} a {pc}!')
else:
    print(f'Você ganhou de {humano} a {pc}!')
