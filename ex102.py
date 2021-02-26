def fatorial(n=1, show=False):
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == True and c > 1:
            print(f'{c} x ', end='')
        else:
            print(f'{c} = ', end='')
    print(f)


fatorial(5, True)
