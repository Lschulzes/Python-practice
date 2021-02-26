import module115


while True:
    opção = module115.optionmenu('MENU PRINCIPAL')
    if opção == 1:
        module115.showlist('PESSOAS CADASTRADAS', 'lista155.txt')
    elif opção == 2:
        module115.writelistname('Nome: ', 'lista155.txt')
        module115.writelistage('Idade: ', 'lista155.txt')
    elif opção == 3:
        module115.optionsair('Saindo do sistema... Até logo!')
        break
    else:
        print('Opção inválida, tente novamente.')
