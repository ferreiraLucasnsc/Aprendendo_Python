# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.google.com.br')
except:
    print('\033[31mERRO:\033[m o site não pode ser acessado')
else:
    print('O site pode ser acessado sem problemas!')