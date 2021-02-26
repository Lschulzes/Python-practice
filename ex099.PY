from time import sleep


def maior():
    valores = []
    while True:
        num = int(input('Digite um valor (999 p/ sair): '))
        if num == 999:
            break
        else:
            valores.append(num)
    quantidade = len(valores)
    maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for i in range(0, quantidade):
        print(valores[i], end=' ', flush=True)
        sleep(0.25)
        if valores[i] > maior:
            maior = valores[i]
    print(f'Foram informados {quantidade} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    print('-=' * 30)


maior()
maior()
maior()
maior()
maior()
