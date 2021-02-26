preço = float(input('Digite o valor do produto a ser pago: '))
modo = 1
vezes = 1
forma = int(
    input('Pagando no dinheiro ou cheque? Digite 1, no cartão? Digite 2! '))
if forma != 1:
    modo = int(
        input('Para pagamento à vista digite 1, ou digite 2 para pagamento parcelado: '))
    if modo == 2:
        vezes = int(input('Quantas vezes deseja parcelar? '))
        if vezes < 3:
            print(f'O custo do produto vai sair por R${preço}')
        else:
            print(f'O custo do produto vai sair por R${preço * 1.2}')
    else:
        print(f'O custo do produto vai sair por R${preço * 0.95}')
else:
    print(f'O custo do produto vai sair por R${preço * 0.9}')
