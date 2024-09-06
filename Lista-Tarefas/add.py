from lista import x



def add_lista():
    while True: 
        try:
            item = input("Digite oque quer adicionar a lista:\n")
            x.append(item)
            op = int(input('Dejeja adicionar mais itens? 1-Sim 2-Não: '))
            if op == 2:
                break   
        except:
           print('Valor invalido, tente novamente') 
           return add_lista()    
    
    print('\n Pressione Enter para voltar ao menu')
        

  