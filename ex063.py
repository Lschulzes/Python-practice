n = int(input('Digite a quantidade de elementos da sequência de fibonacci que você deseja ver: ')) - 2
t1 = 0
t2 = 1
print(t1, '->', t2, '->', end='')
while n > 0:
    n -= 1
    tn = t1 + t2
    print(tn, '->', end='')
    t1 = t2
    t2 = tn
print('FIM')
