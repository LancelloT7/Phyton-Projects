#Receba 3 numeros e exiba o maior

'''numero1 = int(input('Digite o primeiro nummero: '))
numero2 = int(input('Digite o segundo nummero: '))
numero3 = int(input('Digite o terceiro nummero: '))

if numero1 > numero2 and numero1 > numero3:
    maior = numero1
elif numero2 > numero3 and numero2 > numero1:
    maior = numero2
else:
    maior=numero3          

print(f'O maior numero é o {maior}')  '''

# Receber um numero e verificar se é positivo ou negativo

'''numero = int(input('Digite um numero: '))

if numero > 0:
    print('Positivo')
elif numero < 0: 
    print('Negativo')
else:
    print('Numero invalido')'''

    #01  Tabuada
'''n = int(input('Insira um numero: '))
i=1

while i <= 10:
    print(f'{n} X {i} = {i*n}')
   i += 1'''

# Receber notas    
'''while True:
   # nota = int(input('Insira a nota: ' ))
    if nota >= 0 and nota <= 10:
        print(f'nota armazenada {nota}')
       break

   print('Nota invalida')'''

#Tela de Login

'''usuario = (input('Digite um login: ')) 
senha = (input('Digite uma senha: '))

while True:
    login_usuario = input('Digite seu login: ')
    login_senha = input('Digite sua senha: ')
    if login_usuario == usuario and login_senha == senha:
        print('LOGADO')
        break
    else: 
        print('Usuário ou senha invalidos tente novamente')'''

# Receba 10 valores e exiba a soma de todos eles

'''valores =[int(input('Digite 5 numeros')) for i in range(0, 5)]

soma = 0
for i in valores:
    soma = soma + i

print(soma)'''

#Exercicio cadastro de pessoas com lista e dicionários

'''pessoas=[]

while True:
    opcao = int(input('Deseja cadastrar uma pessoa ? (1/sim (2/não)'))
    if opcao == 2:
        break
    
    pessoa = {'nome':input('Digite um nome: '), 'idade': input('Digite a idade: ')}
    pessoas.append (pessoa)

for pessoa in pessoas:
        print( pessoa['nome'], pessoa['idade'] )'''


    
    
        



