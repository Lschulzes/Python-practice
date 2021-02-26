classificação = ('Inter', 'Flam', 'Atl-MG', 'SP', 'Flum', 'Palm', 'Grêmio', 'Santos', 'Ath-PR', 'Cor',
                 'Bragan', 'Ceará', 'Atl-GO', 'Sport', 'Fort', 'BH', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')
for c in range(0, len(classificação)):
    if c < 5:
        print(f'O time {classificação[c]} ficou na colocação [{c + 1}]')
    if c > 14:
        print(f'O time {classificação[c]} ficou na colocação [{c + 1}]')
print(sorted(classificação))
print(classificação.index('Ceará'))
