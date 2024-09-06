from dao import ProdutoDao
from model import Produto

class ProdutoController:
    @classmethod
    def cadastrar(cls, ptn, serie):

        if len(ptn) > 1 and serie >0:
            try:
                ProdutoDao.salvar(Produto(ptn, serie))
                return True
            except:
                return False
        else:
            return False
        
