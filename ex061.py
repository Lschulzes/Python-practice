i = 0
num = int(input('Primeiro termo: '))
r = int(input("Razão da PA: "))
while i < 10:
    print(num, '-> ', end='')
    num += r
    i += 1
print('FIM')
