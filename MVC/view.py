from controller import PessoaController
from dal import PessoaDal


while True:
    op = int(input('Digite 1 para salvar ou 2 para ver a pessoa salva e 3 para sair\n'))
    if op == 3:
        break
    if op ==1:
        nome = input('Digite seu nome: ')
        idade = int(input('Digite sua idade: '))
        cpf = input('Digite o CPF: ')
        if PessoaController.cadastrar(nome, idade, cpf):
            print('Usuário cadastrado')
        else: 
            print('Digite um valor válido')    
    if op == 2:
       print(PessoaDal.ler())      


