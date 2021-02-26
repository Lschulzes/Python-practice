idade = int(input('Qual a sua idade? '))
imovel = int(input('Qual o valor do imóvel? '))
tempo = int(input('Em quantos anos pretende pagar a casa? '))
sal_30 = int(input('Qual o seu salário atual? ')) * 0.3
mensalidade = imovel / (tempo * 12)
if idade + tempo < 60:
    if sal_30 > mensalidade:
        print(
            f'Seu empréstimo foi aprovado com a mensalidade de R${mensalidade:.2f}!')
    else:
        print(f'Seu empréstimo foi negado.')
else:
    print('O tempo de contrato é muito longo, empréstimo negado.')
