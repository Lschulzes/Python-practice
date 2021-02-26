nums = int(input('Digite 3 números: '))
un = nums // 1 % 10
dez = nums // 10 % 10
cent = nums // 100 % 10
if un > dez:
    if un > cent:
        if cent < dez:
            print(f'O maior número é {un} e o menor é {cent}')
        else:
            print(f'O maior número é {un} e o menor é {dez}')
    else:
        print(f'O maior número é {cent} e o menor é {dez}')
elif un > cent:
    print(f'O maior número é {dez} e o menor é {cent}')
elif dez > cent:
    print(f'O maior número é {dez} e o menor é {un}')
else:
    print(f'O maior número é {cent} e o menor é {un}')
