frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for a in range(len(junto) - 1, -1, -1):
    inverso += (junto[a])
if inverso == junto:
    print('A frase é um palíndromo!')
else:
    print('Nada demais aqui.')
