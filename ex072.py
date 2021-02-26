numeros = ('Zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'VINTE!')
while True:
    c = int(input('Digite um número de zero até 20 (30 para sair): '))
    if c == 30:
        break
    elif c >= 0 and c <= 20:
        print(numeros[c])
    else:
        print('Número inválido, tente novamente.')
