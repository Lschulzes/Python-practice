def escreva():
    parametro = input('Digite sua mensagem: ')
    contagem = len(parametro)
    print('-' * (contagem + 4))
    print(f'  {parametro}')
    print('-' * (contagem + 4))


for i in range(0, 3):
    escreva()
