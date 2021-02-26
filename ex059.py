from time import sleep


option = 0
while option != 5:
    if option == 0 or option == 4:
        num_1 = float(input('Digite o primeiro valor: '))
        num_2 = float(input('Digite o segundo valor: '))
    option = int(input(
        '''[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5]Sair do programa\nSua opção: '''))
    if option == 1:
        print(f'{num_1} + {num_2} = {num_1 + num_2}')
        sleep(2)
    elif option == 2:
        print(f'{num_1} x {num_2} = {num_1 * num_2}')
        sleep(2)
    elif option == 3:
        if num_1 > num_2:
            print(f'O maior número é {num_1}')
            sleep(2)
        else:
            print(f'O maior número é {num_2}')
            sleep(2)
    elif option == 5:
        print('Um prazer tê-lo(a) conosco!')
    else:
        print('Opção inválida, tente novamente!')
        sleep(2)
