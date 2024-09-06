

def calculo():
    valor = 0  # Inicializa o valor fora do loop para acumular corretamente

    while True:
        try:
            soma = int(input('Digite a polegada: '))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue  # Se o valor não for um número, reinicia o loop

        if soma == 40:
            valor += 100
        elif soma == 60:
            valor += 150
        else:
            print("Polegada não reconhecida. Tente 40 ou 60.")

        op = input('Deseja cadastrar mais? (1)Sim (2)Não: ')
        if op == '2':
            break

    print(f"Valor total: {valor}")     

calculo()
