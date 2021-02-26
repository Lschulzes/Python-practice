num = int(input('Digite um número inteiro: '))
primo = True
for a in range(2, num):
    if num % a == 0:
        primo = False
if primo == True:
    print(f'{num} é um número primo!!')
else:
    print(f'{num} não é um número primo!!')
