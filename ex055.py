maior = 0
menor = 0
for a in range(0, 5):
    peso = int(input('Digite o peso da pessoa: '))
    if maior == 0:
        maior = peso
    if menor == 0:
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O maior peso é de {maior} Kgs e o menor é de {menor} Kgs!')
