def notas(*n, sit=False):
    dicio = {}
    dicio['total'] = len(n)
    dicio['maior'] = 0
    dicio['menor'] = 0
    média = soma = 0
    for i in range(0, len(n)):
        soma += n[i]
        if i == 0:
            dicio['maior'] = n[i]
            dicio['menor'] = n[i]
        elif n[i] > dicio['maior']:
            dicio['maior'] = n[i]
        elif n[i] < dicio['menor']:
            dicio['menor'] = n[i]
    média = soma / len(n)
    dicio['média'] = média
    if sit == True:
        if média >= 7:
            dicio['situação'] = 'Boa'
        elif média < 5:
            dicio['situação'] = 'Ruim'
        else:
            dicio['situação'] = 'Razoável'
    return dicio


resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
