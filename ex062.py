i = 0
num = int(input('Primeiro termo: '))
r = int(input("Razão da PA: "))
while i < 10:
    print(num, '-> ', end='')
    num += r
    i += 1
quantidade = 1
while quantidade != 0:
    if quantidade == 1:
        quantidade = int(
            input('\nDeseja ver mais quantos termos? digite 0 para encerrar o programa. ')) + 1
        if quantidade == 1:
            quantidade = 0
    else:
        quantidade -= 1
        num += r
        print(num, '-> ', end='')
