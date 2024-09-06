from lista import x



def remover():  
    while True:
        removido = input('Digite qual item deseja remover da lista: ')
        if removido in x:
             x.remove(removido)
        else:
             print('Item não encontrado')

        op = int(input('Deseja remover mais itens da lista ? 1-Sim 2-Não: '))  
        if op == 2:
            break
        elif op !=1:
            print('Opção invalida encerrando')
            break
        

