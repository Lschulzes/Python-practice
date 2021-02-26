def leiaint(msg):
    while True:
        n = input(msg)
        if n.isalpha():
            print('ERRO! Digite um número inteiro válido.')
        elif n.isspace():
            print('ERRO! Digite um número inteiro válido.')
        elif n.isnumeric():
            n = int(n)
            break
        else:
            print('ERRO! Digite um número inteiro válido.')
    return n


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
