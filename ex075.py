valores = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(
    input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os valores {valores}')
nove = valores.count(9)
par = 0
print(f'O valor 9 apareceu {nove} vezes')
if 3 in valores:
    tres = valores.index(3) + 1
    print(f'O valor 3 apareceu na {tres}ª posição')
else:
    print('Você não digitou o número 3')
print('Os valores pares digitados foram: ', end='')
for a in range(0, len(valores)):
    if valores[a] % 2 == 0:
        print(valores[a], end=' ')
