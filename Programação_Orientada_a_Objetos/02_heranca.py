'''
class Pessoa:                  #Classe pai

    def falar(self):
        print('Estou falando')

    def andar(self):
        print('Estou andado')

class Cliente(Pessoa):    #Classe cliente herdando da classe Pessoa
    
    def comprar(self):
        print('Estou comprando')
    
class Vendedor(Pessoa):  #Classe Vendedor herdando da classe Pessoa

    def vender(self):
        print('Estou vendendo')
        
c1 = Cliente() 

c1.falar()
c1.andar()
c1.comprar()

v1 = Vendedor()

v1.falar()
v1.andar()
v1.vender()'''

# Sobreposição de métodos
'''
class Pessoa:                  #Classe pai

    def falar(self):
        print('Estou falando')

    def andar(self):
        print('Estou andado')

    def comprar(self):          # Método que será sobrescrito
        print('Estou comprando')   

class Cliente(Pessoa):    #Classe cliente herdando da classe Pessoa
    
    def comprar(self):    #Sobrescrevendo o método para mudar a frase exibida
        print('Comprando') # Alterado da classe original
        super().comprar()  # Buscando e forçando a execução do método da classe Pai
   
    
class Vendedor(Pessoa):  #Classe Vendedor herdando da classe Pessoa

    def vender(self):
        print('Estou vendendo')

c1 = Cliente() 

c1.comprar()    '''

# Criando Classes e fazendo com que herdem atributos da classe pai
'''
class Pessoa:  # Classe Pai

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Cliente(Pessoa):

    def __init__(self, id_cliente, nome, cpf):  # Id_cliente é um atributo exclusivo da classe cliente que herda da classe Pessoa os atributos (nome, cpf)
        super().__init__(nome, cpf) # Neste trecho a classe Cliente herda os atributos da classe pai 
        self.id_cliente = id_cliente


c1 = Cliente(2, 'Gabriel Matias', 123456)

print(c1.id_cliente)
print(c1.nome)
print(c1.cpf)

class Vendedor(Pessoa):

    def __init__(self, vendas, nome, cpf):
        super().__init__(nome,cpf)
        self.vendas = vendas

v1 = Vendedor('Carro', 'Nicoli', 5555555)

print(v1.vendas)
print(v1.nome)
print(v1.cpf)'''

# Herança multipla
'''
class Animal:
    def andar(self):
        print('Estou andando como um animal')

    def correr(self):
        print('Estou correndo')

    def pular(self):
        print('estou pulando ')

class Felino (Animal):
    def felino(self):
        print('Eu sou um felino')

class Cachorro(Animal):
    def latir(self):
        print('Estou latindo')

class Gato (Felino): # Gato herda da Classe Felino que por sua vez herda da Classe Animal, sendo assim além do próprio método a classe Gato também herda os métodos de Felino e Animal sendo assim uma herança multipla
    def miar(self):
        print('Estou miando')             

y = Gato()
y.felino()
y.andar()
y.correr()
y.pular()
y.miar()
'''
