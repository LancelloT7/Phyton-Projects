from model import Pessoa



class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa): # Recebendo os atributos da classe Pessoa que está na model
        with open('pessoa.txt', 'w') as arq: 
            arq.write(pessoa.nome + " "+ str(pessoa.idade)+" "+pessoa.cpf)
    @classmethod
    def ler(cls):
        nome = 'Gabriel1'
        idade = 20
        cpf = '42326396839'
        return Pessoa(nome, idade, cpf)  
    

    
    


