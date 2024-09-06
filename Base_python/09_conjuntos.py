# Obs: Conjuntos não permitem dados repetidos

'''x = [1,1,1,2,2,2,3,3,3,] # Lista
x = set(x) # Convertendo uma lista em conjunto 
print(x)'''

# Para inserir diretamente um conjunto devemos usar a variavel = {valor,valor} exemplo como no abaixo

'''x ={1,1,2,2,3,3,4,4,5,5}

print(x)'''

# Unindo conjuntos

'''x ={1,2,3,4,5}
y ={5,6,7,8,9,10}

x = x.union(y)

print(x)'''

# Interseção entre conjuntos

'''x ={1,2,3,4,5,6}
y ={5,6,7,8,9,10}

x = x.intersection(y)
print(x)'''

# Diferença entre conjuntos

'''x ={1,2,3,4,5,6}
y ={5,6,7,8,9,10}

x = x.difference(y)
print(x)'''

# Exibindo os valores dos conjuntos ignorando a interseção entre eles

'''x ={1,2,3,4,5,6}
y ={5,6,7,8,9,10}

x = x.symmetric_difference(y)
print(x)'''





