# Filtrando item em uma lista
'''
x = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

pesquisa = input('Digite o valor procurado')
if pesquisa == filter(list(x)):
    print(pesquisa)
else:
    print('Valor não encontrado')'''

# Código para uma pesquisa de itens pré cadastrados
'''
x = [{'ptn': 12, 'serie': 1, 'sku':111},
     {'ptn': 13, 'serie': 2, 'sku':000},
     {'ptn': 14, 'serie': 3, 'sku':123}]

pesquisa = int(input('Digite o valor procurado: '))
resultado = None

for item in x:
    if item['ptn'] == pesquisa:
        resultado = item
        break

if resultado:
    print(f'PTN: {resultado['ptn']}')
    print(f'serie: {resultado['serie']}')
    print(f'sku: {resultado['sku']}')
else:
    print('Valor não encontrado')'''


        


