numero = int(input('Digite um número inteiro qualquer: '))
conv = int(input(
    'Escolha uma base de conversão, digite 1 para binário, 2 para octal e 3 para hexadecimal: '))
if conv == 1:
    print(bin(numero)[2:])
elif conv == 2:
    print(oct(numero)[2:])
elif conv == 3:
    print(hex(numero)[2:])
else:
    print('Opção inválida!')
