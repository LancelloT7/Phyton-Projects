nota1 = int(input ('Digite sua primeira nota: '))
nota2 = int(input ('Digite sua segunda nota: '))
nota3 = int(input ('Digite sua terceira nota: '))
nota4 = int(input ('Digite sua quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 6:
    print(f'Aprovado sua media é: {media}')
elif media >= 4:
    print(f'recuperação sua media é: {media}')
else:
    print(f'reprovado sua media é: {media}')   
