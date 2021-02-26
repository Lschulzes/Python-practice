def area():
    l = float(input('LARGURA (m): '))
    c = float(input('COMPRIMENTO (m): '))
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m²')


print('  CONTROLE DE TERRENOS')
print('-' * 40)
area()
