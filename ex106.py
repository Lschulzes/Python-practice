def ajuda():
    from time import sleep
    while True:
        print('-' * 30)
        print(f'  SISTEMA DE AJUDA PyHELP')
        print('-' * 30)
        parametro = input('Função ou Biblioteca > ').strip().lower()
        if parametro == 'fim':
            print('-' * 20)
            print(f'  ATÉ LOGO')
            print('-' * 20)
            break
        contagem = len(parametro)
        print('-' * (contagem + 38))
        print(f'  Acessando o manual do comando  \'{parametro}\'')
        print('-' * (contagem + 38))
        sleep(0.5)
        help(parametro)


ajuda()
