from model import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open ('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria)) # Retirando os \n do texto usando programação funcional
        
        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))

        return cat    


class DaoVenda:
    @classmethod
    def salvar(cls, venda : Venda):
        with open('venda.txt', 'a') as arq:
            arq.writelines(venda.itensVendidos.nome + "|" + venda.itensVendidos.preco + "|" + venda.itensVendidos.categoria + "|" + venda.vendedor + "|" + venda.comprador + "|" + str(venda.quantidadeVendida + "|" + venda.data))
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arq:
            cls.venda = arq.readlines()     

        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda)) # Retirando os \n do texto usando programação funcional
        cls.venda = list(map(lambda x: x.split('|'), cls.venda)) # Retirando os " | " do texto usando programação funcional
        vend = []
        for i in cls.venda:
            vend.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        return vend
    

class DaoEstoque:
    @classmethod
    def salvar(cls, produtos: Produtos, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produtos.nome + "|" + produtos.preco + "|" + produtos.categoria  + "|" + str(quantidade))
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque)) # Retirando os \n do texto usando programação funcional
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque)) # Retirando os " | " do texto usando programação funcional 
        est = []            
        for i in cls.estoque:
            est.append(Estoque(Produtos(i[0], i[1], i[2]), i[3]))
        return est

class DaoFornecedor:
    @classmethod
    def salvar(cls, forncedor: Fornecedor):
        with open('fornecedores.txt', 'a') as arq:
            arq.writelines(forncedor.nome + "|" + forncedor.cnpj + "|" + forncedor.telefone + "|" + forncedor.categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('forncedores.txt', 'r') as arq:
            cls.fornecedores = arq.readlines()

        cls.forncedores = list(map(lambda x: x.replace('\n', ''), cls.forncedores)) # Retirando os \n do texto usando programação funcional
        cls.fornecedores = list(map(lambda x: x.split('|'), cls.fornecedores)) # Retirando os " | " do texto usando programação funcional 
        forn = []            
        for i in cls.forncedores:
            forn.append(Fornecedor(i[0], i[1], i[2], i[3]))
        return forn

class DaoPessoa:
    @classmethod
    def salvat(cls, pessoa : Pessoa):
        with open('clientes.txt', 'a') as arq:
            arq.writelines = ( pessoa.nome + "|" + pessoa.telefone + "|" + pessoa.cpf + "|" + pessoa.email + "|" + pessoa.endereço )
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open ('clientes.txt', 'r') as arq:
            cls.clientes = arq.readlines()

        cls.clientes = list(map(lambda x: x.replace('\n', ''), cls.clientes)) # Retirando os \n do texto usando programação funcional
        cls.clientes = list(map(lambda x: x.split('|'), cls.clientes)) # Retirando os " | " do texto usando programação funcional 
        clientes = []            
        for i in cls.clientes:
            clientes.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
        return clientes    

class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionarios.txt', 'a') as arq:
            arq.writelines = (funcionario.clt + "|" + funcionario.nome + "|" + funcionario.telefone + "|" + funcionario.cpf + "|" + funcionario.email + "|" + funcionario.endereço)
            arq.writelines('\n')

    def ler(cls):
        with open('funcionarios.txt', 'r') as arq:
            cls.funcionarios = arq.readlines() 

        cls.funcionarios = list(map(lambda x: x.replace('\n', ''), cls.funcionarios)) # Retirando os \n do texto usando programação funcional
        cls.funcionarios = list(map(lambda x: x.split('|'), cls.funcionarios)) # Retirando os " | " do texto usando programação funcional 
        funcionario = []            
        for i in cls.funcionarios:
            funcionario.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))
        return funcionario
    


    



