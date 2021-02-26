palavras = ('clave', 'enxada', 'ferrugem', 'loucura')
for a in palavras:
    print(f'\nNa palavra {a} temos ', end='')
    for letra in a:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
