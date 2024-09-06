# Criando um dicionário

'''x = {'nome': 'Gabriel', 'idade':29, 'cep': '07956040'}


print (x['nome'])
print (x['idade'])
print (x['cep'])'''

# Alterando um valor no dicionário

'''x = {'nome': 'Gabriel', 'idade':29, 'cep': '07956040'}

x['nome'] = 'Noah'
x['idade'] = '5 meses'


print (x['nome'])
print (x['idade'])
print (x['cep'])'''

# Criando listas dentro do dicionário

'''x = {'nomes':[], 'idade':29}

x['nomes'].append('Gabriel')
x['nomes'].append('Noah')

print(x['nomes'][0])'''

# Criando dicionários dentro de uma lista

'''pessoas =[{'nome': 'Gabriel', 'idade':29},
          {'nome': 'Nicoli', 'idade':28},
          {'nome': 'Noah', 'idade':0}]

for pessoa in pessoas:
    print(pessoa)
    print(pessoa['nome'])# Consultado campo espcifico no dicionário'''

# Exercicio cadastro de pessoas com lista e dicionários

'''pessoas=[]

while True:
    opcao = int(input('Deseja cadastrar uma pessoa ? (1/sim (2/não)'))
    if opcao == 2:
        break
    
    pessoa = {'nome':input('Digite um nome: '), 'idade': input('Digite a idade: ')}
    pessoas.append (pessoa)

for pessoa in pessoas:
        print( pessoa['nome'], pessoa['idade'] )'''

# Funções para consultas em dicionários

'''pessoa = {'nome': 'Gabriel', 'idade':29, 'cep': '07956040'}
print(pessoa.items()) # Mostra tantos as chaves quanto os valores
print(pessoa.values()) # Mostra valores armazenados
print(pessoa.keys()) # Mostra as chaves existentes'''

# Iterando sobre listas com consultas especificas

'''pessoa = {'nome': 'Gabriel', 'idade':29,}

for i, j in pessoa.items():
    print(f"{i}  {j}")'''









