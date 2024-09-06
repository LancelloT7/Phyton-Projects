# Lista Simples

'''nomes = ['Gabriel', 'Nicoli', 'Noah']


print(nomes[2])
print(len(nomes))'''

# Alterando Valores na lista

'''nomes = ['Gabriel', 'Nicoli', 'Noah']

nomes[0] = "Gabriem Matias"
print(nomes[0])
print(len(nomes))'''

# Adicionando Elementos na lista (append)

'''nomes = ['Gabriel', 'Nicoli', 'Noah']

nomes.append('Lucia')
print(nomes[3])
print(len(nomes))'''

#Criando uma lista com input

'''nomes =[]
while True:
    nome = input('Digite -1 para sair ou cadastre um nome: ')
    if nome == "-1":
     break

    nomes.append(nome)

print(nomes)'''

# Adicionando valores em posições espcificas da lista com input (insert)

'''nomes =['Gabriel', 'Nicoli', 'Noah' ]
nomes.insert(0, 'Gabriel Matias')

print(nomes[0])'''

# Removendo Valores na lista artavés da posição (pop)

'''nomes =['Gabriel', 'Nicoli', 'Noah' ]
nomes.pop(0)

print(nomes)'''

# Removendo Valores através do valor dentro da lista (remove)

'''nomes =['Gabriel', 'Nicoli', 'Noah' ]
nomes.remove('Gabriel')

print(nomes)'''

# Descobrindo a posição dos elementos na lista (index)

'''nomes =['Gabriel', 'Nicoli', 'Noah' ]
nomes.index('Gabriel')

print(nomes.index('Gabriel'))'''

# Ordenando Lista em ordem crescente (sorti)

'''nomes =['Noah', 'Gabriel', 'Nicoli']
nomes.sort()

print(nomes)'''

#  Ordenando Lista em ordem decrescente (sort(reverse=True))

# Ordenando Lista em ordem crescente (sorti)

'''nomes =['Noah', 'Gabriel', 'Nicoli']
nomes.sort(reverse=True)

print(nomes)'''

# Ordenando Lista em ordem crescente sem alterar a lista original (sorted)

'''nomes =['Noah', 'Gabriel', 'Nicoli']
nomes_ordenados = sorted(nomes)

print(nomes_ordenados)'''

# Iterando sobre a lista 

'''nomes =['Noah', 'Gabriel', 'Nicoli']


for i, j in enumerate(nomes):

    print(i, j)'''

#  Criando uma matrix

'''idades = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

print(idades[1][2])'''

# Iterando sobre a matrix

'''idades = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

for i in range(0, len(idades)):
    print(idades[i])'''

# List comprehension simples

'''x = [i for i in range(1, 11)]

print(x)'''

# List comprehension complexa

'''x = [input('Digite um nome: ') for i in range(0, 3)]
 
print (x)'''






    



