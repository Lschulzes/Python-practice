def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido\033[m')
        except (KeyboardInterrupt):
            print('\033[0;31mUsuário prefiriu não digitar\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido\033[m')
        except (KeyboardInterrupt):
            print('\033[0;31mUsuário prefiriu não digitar\033[m')
            return 0
        else:
            return n


i = leiaint('Digite um inteiro: ')
r = leiafloat('Digite um real: ')
print(i)
print(r)
