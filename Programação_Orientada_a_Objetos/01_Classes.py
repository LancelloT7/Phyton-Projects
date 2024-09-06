# Construindo uma classe em Python
'''
class Pessoas:
    def __init__(self, nome, idade, cpf): # Self instancia todos os atributos sem ele não será possivel instaciar os atributos junto com a classe
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def logar_sistema(self): #Método da Classe
        print(f'{self.nome} logando no sistema')

p1 = Pessoas('Gabriel', 29, 42326396839)
p2 = Pessoas('Nicoli', 29, 00000000)


p1.logar_sistema()
p2.logar_sistema()'''

# Classe com método construtor
'''
class Pessoas:
    def __init__(self, nome, idade, cpf): # Init representa o Construtor, 
        print(f'{nome} | {idade} | {cpf}')
    def logar_sistema(self): #Método da Classe
        print('Estou logando no sistema')

p1 = Pessoas('Gabriel Matias', 29, '000000')'''

# Atributos da classe são diferentes de atributos de instancia e podem ser acessado sem que exista uma instancia da classe
'''
class Pessoas:
    possui_nome = True          #Linha 32 e 33 são atributos da classe, linhas 36, 37, 38 são atributos da instancia
    possui_raca = 'Ser humano'

    def __init__(self, nome, idade, cpf): # Self instancia todos os atributos sem ele não será possivel instaciar os atributos junto com a classe
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def logar_sistema(self): #Método da Instancia
        print(f'{self.nome} logando no sistema')

p1 = Pessoas('Gabriel', 29, 42326396839)
p1.logar_sistema()
print(Pessoas.possui_nome)
print(Pessoas.possui_raca) '''

# Métodos de classe
'''
class Pessoas:
    possui_nome = True          #Linha 32 e 33 são atributos da classe, linhas 36, 37, 38 são atributos da instancia
    possui_raca = 'Ser humano'

    def __init__(self, nome, idade, cpf): # Self instancia todos os atributos sem ele não será possivel instaciar os atributos junto com a classe
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def logar_sistema(self): # Método da instancia
        print(f'{self.nome} logando no sistema')
    
    @classmethod         # @classmethod identifica que é um método da classe que indepnde da instacia pra ser acessado
    def andar(cls):      # Self aponta para a instancia enauqnto cls aponta para classe
        print ('Estou andando')   

p1 = Pessoas('Gabriel', 29, 42326396839)

print(Pessoas.possui_nome)
print(Pessoas.possui_raca)
p1.logar_sistema()
p1.andar()       # Conseguimos acessar métodos de classe através da instancia pois a intancia também é uma classe
Pessoas.andar()  # E Conseguimos acessar diretamente sem precisar instanciar '''

# Utilizando o CLS
'''
class Pessoas:
    possui_nome = True          #Linha 32 e 33 são atributos da classe, linhas 36, 37, 38 são atributos da instancia
    possui_raca = 'Ser humano'

    def __init__(self, nome, idade, cpf): # Self instancia todos os atributos sem ele não será possivel instaciar os atributos junto com a classe
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def logar_sistema(self): # Método da instancia
        print(f'{self.nome} logando no sistema')
    
    @classmethod                # @classmethod identifica que é um método da classe que indepnde da instacia pra ser acessado
    def andar(cls):             # Self aponta para a instancia enauqnto cls aponta para classe
        cls.cor_preferida = 'Preto'  # Com o CLS foi possivel criar uma vairavel na classe e adicionar um valor sem que precise instanciar 
        cls.possui_nome = False # Com o CLS foi possivel alterar o valor de uma variavel da classe
        return None

p1 = Pessoas('Gabriel', 29, 42326396839)

print(Pessoas.possui_nome)
print(Pessoas.possui_raca)

p1.logar_sistema()
p1.andar()       # Conseguimos acessar métodos de classe através da instancia pois a intancia também é uma classe
Pessoas.andar()  # E Conseguimos acessar diretamente sem precisar instanciar
print(Pessoas.possui_nome) '''

# utilizando métodos estáticos
'''
class Pessoas:
    possui_nome = True          #Linha 32 e 33 são atributos da classe, linhas 36, 37, 38 são atributos da instancia
    possui_raca = 'Ser humano'

    def __init__(self, nome, idade, cpf): # Self instancia todos os atributos sem ele não será possivel instaciar os atributos junto com a classe
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def logar_sistema(self): # Método da instancia
        print(f'{self.nome} logando no sistema')
    
    @classmethod                # @classmethod identifica que é um método da classe que indepnde da instacia pra ser acessado
    def andar(cls):             # Self aponta para a instancia enauqnto cls aponta para classe
        cls.cor_preferida = 'Preto'  # Com o CLS foi possivel criar uma vairavel na classe e adicionar um valor sem que precise instanciar 
        cls.possui_nome = False # Com o CLS foi possivel alterar o valor de uma variavel da classe
        return None
    
    @staticmethod        # @staticmethod define que será um método estático
    def e_adulto(idade): # Métodos estáticos são apenas consultivos, não tem acesso aos métodos nem atributos de classe 
        if idade > 18:
            return True
        else:
            return False
            

p1 = Pessoas('Gabriel', 29, 42326396839)

print(Pessoas.possui_nome)
print(Pessoas.possui_raca)

p1.logar_sistema()
p1.andar()       # Conseguimos acessar métodos de classe através da instancia pois a intancia também é uma classe
Pessoas.andar()  # E Conseguimos acessar diretamente sem precisar instanciar
print(Pessoas.possui_nome)
print(Pessoas.e_adulto(21))'''










