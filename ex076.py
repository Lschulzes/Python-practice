listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
            'Estojo', 25.00, 'Canetas', 22.30, 'Livro', 34.90)

for a in range(0, len(listagem), 2):
    ddd = 30 - len(listagem[a])
    print(f'{listagem[a]}', '.' * ddd, f'R$ {listagem[a + 1]: >4}')
