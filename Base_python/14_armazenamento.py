# Armazendano dados de forma persistente em um aquivo de texto (w = Escrever) (a = Adicionar) (r = Ler)

# Escrevendo no arquivo
'''
arquivo = open('pessoas.txt', 'w')
arquivo.write('ola\n')'''

# Adicionando ao arquivo
'''
arquivo = open('pessoas.txt', 'a')
arquivo.write('ola\n')'''

# Lendo o texto do arquivo
'''
arquivo = open('pessoas.txt', 'r')
resultado = arquivo.readline()
print (resultado)'''

# Iterando sobre o arquivo
'''
arquivo = open('pessoas.txt', 'r')
resultado = arquivo.readlines()
for i in resultado:
    print(i)'''

# Usando o (with) para fechar o arquivo automaticamente assim que sairmos dele
'''
with open('pessoas.txt', 'r') as arq:
    x = arq.read()
    print(x)'''

# Serialização de dados (dumps)
'''
import pickle

x = [1, 2, 3, 4] 

print(pickle.dumps(x)) # O dumps serializa os dados em binário

string = pickle.dumps(x) # Repassando para outra variavel o valor convertido em binário
print(pickle.loads(string)) # Usando pickle.loads para reconverter para o valor original'''

# Serializando dados (dump)
'''
import pickle

x = [1, 2, 3, 4] 

arq = open('arquivo.pkl', 'wb') # (wb) Diz que vamos escrever no arquivo mas que será salvo de forma binária
pickle.dump(x, arq)

arq = open('arquivo.pkl', 'rb') # (rb) Diz que vamos ler o arquivo que está em formato binário
retornou = pickle.load(arq) # Reconverte o arquivo para o valor original

print(retornou)'''