from add import add_lista
from print import mostrar
from remover import remover

def menu():
    while True:
        op = int(input("Digite o numero da opção desejada: \n01-Adicionar a lista\n02-Remover item da lista\n03-Ver Lista\n04-Sair"))
        if op == 1:
            add_lista()
        elif op == 2:
            remover() 
        elif op == 3:
            mostrar()
        elif op == 4:
            print('Saindo')
            break
        else:
            print('Opção invalida tente novamente')
            return menu()
                 

menu()