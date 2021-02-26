quantidade = soma = 0


while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    else:
        quantidade += 1
        soma += num
print(f'A soma dos {quantidade} números digitados foi de {soma}')
