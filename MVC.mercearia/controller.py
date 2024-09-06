from model import Categoria, Estoque, Fornecedor, Pessoa, Funcionario, Venda
from dao import DaoCategoria, DaoVenda, DaoEstoque, DaoFornecedor, DaoPessoa, DaoFuncionario
from datetime import datetime

class ControllerCategoria:
    def cadastrarCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True

        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria Cadastrada com sucesso')
        else:  
            print("A categoria que deseja cadastrar já existe ")  

    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))

        if len(cat) <=0:
            print('A Categoria que deseja remover não existe')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('Categoria Removida com sucesso')  

            with open('categoria.txt', 'w')  as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada)if(x.categoria == categoriaAlterar)else(x),x))
                print('Categoria alterada com sucesso')
            else:
                print ('A categoria para qual deseja alterar já existe ') 

        else:
            print('A categoria que deseja modificar não existe')    

        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria) 
                arq.writelines('\n') 

    def mostrarCategoria(self):
        categoria = DaoCategoria.ler()
        if len(categoria) == 0:
            print('Categoria vazia')            
        else: 
            for i in categoria:
                print(f'Categoria: {i.categoria}')

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()











        




