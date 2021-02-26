nota_1 = float(input('Nota da avaliação 1: '))
nota_2 = float(input('Nota da avaliação 2: '))
media = (nota_1 + nota_2) / 2
if media >= 7:
    print(f'Aprovado com a média {media}')
elif 5 <= media < 7:
    print(f'O aluno se encontra em recuperação com a média {media}')
else:
    print(f'O aluno está reprovado com a média {media}')
