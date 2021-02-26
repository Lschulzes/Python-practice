import random


a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')
alunos = [a, b, c, d]
sorteado = random.choice(alunos)
print(f'O aluno {sorteado} foi sorteado para apagar o quadro!')
