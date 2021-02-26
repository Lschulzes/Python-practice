quantidade = 0
num = int(input('Digite um número: '))
maior = menor = num
soma = 0
sair = False
while sair == False:
    soma += num
    quantidade += 1
    continuar = input('Deseja continuar [S/N]: ').strip().upper()
    if continuar == 'S':
        num = int(input('Digite um número: '))
    elif continuar == 'N':
        sair = True
    else:
        print('Não entendi, digite novamente abaixo.')
        soma -= num
        quantidade -= 1
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
print(
    f'A média dos números digitados foi de [{soma / quantidade}] o maior valor foi de [{maior}] e o menor de [{menor}]')
