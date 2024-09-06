from model import Produto

class ProdutoDao:
     @classmethod
     def salvar(cls, produto: Produto): # Recebendo os atributos da classe Pessoa que está na model
        with open('produto.txt', 'w') as arq: 
            arq.write(produto.ptn + " "+ str(produto.ptn))
     @classmethod
     def ler(cls):
        ptn = '123'
        serie = '456'
        return Produto(ptn, serie)