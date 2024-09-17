# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Chapecoense.

times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'São Paulo', 'Bahia', 'Cruzeiro', 'Parananese',
         'Bragantino', 'Atlético Mineiro', 'Vasco', 'Juventude', 'Internacional', 'Corinthians', 'Criciuma',
         'Cuiabá', 'Vitória', 'Grêmio', 'Fluminense', 'Atlético Goianiense')

print('\t\tANÁLISE DOS TIMES DO BRASILEIRÃO')
print('* Cinco primeiros colocados:')
print(times[:5])
print('* Quatro úlimos colocados:')
print(times[-4:])
print('* Times em ordem alfabética:')
timesAlfa = sorted(times)
c = 0
for t in timesAlfa:
    print(' -', t)
if 'Chapecoense' not in times:
    print(' * O time da Chapecoense não está na primeira divisão')
else:
    print(' * O time da Chapecoense está na', times.index('Chapecoense') + 1, 'posição')