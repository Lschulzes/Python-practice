from random import shuffle


a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')
alunos = [a, b, c, d]
shuffle(alunos)
print(f'A ordem da apresentação será {alunos}')
