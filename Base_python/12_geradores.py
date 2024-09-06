# Geradores (yield) conseguem gerar valores dentro da variavel mas sem ocupar espaço na memoria pois eles geram um valor por vez e não guardam o valor anterior na memoria apenas geram eles momentaneamente 
'''
from pympler.asizeof import asizeof

def dobro(lista):
    for i in lista:
         yield i*2

x = dobro(range(0, 100))

for i in x:
     print(i)'''
