from datetime import date


maiores = 0
for a in range(0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    idade = date.today().year - ano
    if idade >= 20:
        maiores += 1
print(
    f'Desta amostra {maiores} pessoas atingiram a maioridade e {7 - maiores} ainda não!')
