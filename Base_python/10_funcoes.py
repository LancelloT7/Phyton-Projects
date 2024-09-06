# Função simples
'''
def minha_funcao():
    print('Olá')
    print('Tudo bem ?')

minha_funcao()'''  

# Para colocar todos os pametros em uma tupla usamos o *args
# Para colocar todos os pametros em um dicionário usamos o **kwargs


# Usando kwargs + get para pegar um valor 
'''
def minha_funcao(**kwargs):
    x =kwargs.get('teste1')
    print(x)

minha_funcao(teste1=1, teste2=2, teste3=3 )'''

