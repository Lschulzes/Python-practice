num = int(
    input('Digite um número inteiro ou 999 para parar e mostrar o resultado: '))
soma = 0
quantidade = 0
while num != 999:
    soma += num
    quantidade += 1
    num = int(
        input('Digite um número inteiro ou 999 para parar e mostrar o resultado: '))

print(f'Você digitou {quantidade} números e a soma deles é [{soma}]')
