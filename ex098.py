from time import sleep


def contagem(i, f, p):
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    print('-=' * 20)
    atual = i
    while True:
        if p >= 0:
            print(f'{atual}', end='-> ', flush=True)
            sleep(0.25)
        if p == 0:
            p = 1
        if p < 0:
            p = p * (-1)
        elif f < i:
            if atual >= (f + p):
                atual -= p
            else:
                print('FIM!')
                break
        elif atual <= (f - p):
            atual += p
        else:
            print('FIM!')
            break


contagem(1, 10, 1)
contagem(10, 0, 2)
print('-=' * 20)
print('SUA VEZ DE USAR ESTA FUNÇÃO!!')
print('-=' * 20)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contagem(i, f, p)
