num = 0
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('_' * 20)
    if num > -1:
        for a in range(1, 11):
            print(f'{a} x {num} = {a * num}')
        print('_' * 20)
    else:
        break
