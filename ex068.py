from random import randint


vit = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
while True:
    num = int(input('Diga uma valor: '))
    escolha = input('Par ou Ímpar? [P/I] ').upper().strip()
    print('-' * 50)
    compu = randint(0, 10)
    resultado = compu + num
    if resultado % 2 == 0:
        print(
            f'Você jogou {num} e o computador {compu}. O total de {resultado} dá PAR!')
        print('-' * 50)
        if escolha == 'P':
            print('Você GANHOU!')
            vit += 1
        else:
            print('Você PERDEU!')
            print('=-' * 20)
            break
    else:
        print(
            f'Você jogou {num} e o computador {compu}. O total de {resultado} deu ÍMPAR!')
        print('-' * 50)
        if escolha == 'I':
            print('Você GANHOU!')
            vit += 1
        else:
            print('Você PERDEU!')
            print('=-' * 20)
            break
print(f'GAME OVER! Você venceu {vit} vezes!')
