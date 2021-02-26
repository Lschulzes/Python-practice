i = 0
while i == 0:
    try:
        numero = int(input('Digite um número inteiro: '))
        ns = numero + 1
        na = numero - 1
        print(f'O sucessor é {ns} e o antecessor é {na}')
        i = 1
    except:
        print("Digite um número inteiro por favor.")
