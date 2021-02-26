somaidade = 0
homem = ''
idadehomem = 0
mulheres_novas = 0
for a in range(0, 4):
    nome = input('Digite o nome: ').strip()
    idade = int(input('Qual a idade? '))
    sexo = input('Sexo [M/F] ').strip().upper()
    somaidade += idade
    if sexo == 'M' and idade > idadehomem:
        homem = nome
        idadehomem = idade
    if sexo == 'F' and idade < 20:
        mulheres_novas += 1
print(
    f'A idade média do grupo é de {somaidade / 4} anos, o homem mais velho se chama {homem} e há {mulheres_novas} mulher(es) com menos de 20 anos no grupo!')
