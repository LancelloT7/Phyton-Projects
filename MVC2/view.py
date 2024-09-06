from controller import ProdutoController
from dao import ProdutoDao


while True:
    op = int(input('Digite 1 para salvar ou 2 para ver o produto e 3 para sair\n'))
    if op == 3:
        break
    if op ==1:
        ptn = input('Digite o PTN: ')
        serie = int(input('Digite o S/N: '))
        if ProdutoController.cadastrar(ptn, serie):
            print('cadastrado')
        else: 
            print('Digite um valor válido')    
    if op == 2:
       print(f'PTN: {ProdutoDao.ler().ptn}')
       print(f'S/N: {ProdutoDao.ler().serie}')
       


