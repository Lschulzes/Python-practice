import urllib.request

try:
    result = urllib.request.urlopen('http://pudim.com.br/')
    p = result.getcode()
    print('O site pudim está acessível!')
except:
    print('O site pudim não está acessível no momento!')
