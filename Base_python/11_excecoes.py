# Usando o Try e Except o Finaly
'''
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))

try:
    print(n1/n2)
except:
    print('Não foi possivel realizar a divisão')   
finally:
    print('FInalizado')'''   

# Definindo tipos de exceções
'''
try:
    n1 = int(input("Digite um numero: "))
    print(5/n1)
except ValueError:
    print('Digite um numero inteiro')
except ZeroDivisionError: 
    print('Não digite 0')
finally:
    print('FInalizado')'''

# Capturando uma exceção
'''
try:
    n1 = int(input("Digite um numero: "))
    print(5/n1)
except Exception as e:
    print(e)'''

# Forçando uma exceção no código com (raise)
'''
def soma(n1, n2):
    if n1 < 0 or n2 < 0:
        raise ValueError('Os numeros não podem ser negativos')
    return n1 + n2

print(soma(-1, 2))'''

# Forçando uma exceção no código com (raise)
'''
x=-1
assert x > 0, 'O numero não podem ser negativo' '''
