from random import randint


num = (randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10))
print(f'Eu sorteei os valores {num}')
crescente = sorted(num)
print(f'O maior valor é {crescente[4]} e o menor é {crescente[0]}')
