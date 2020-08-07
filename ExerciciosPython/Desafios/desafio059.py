a=(float(input('Digite um número: ')))
b=(float(input('Digite um número: ')))

opcao=int
while opcao != 5:
    opcao=(int(input("""Selecione a operação desejada: 
[1] somar 
[2] multiplicar 
[3] maior 
[4] novos números 
[5] sair
""")))
    if opcao==1:
        print('A soma é de {} e {} é {}.' .format(a, b, a+b))
    elif opcao==2:
        print('O produto de {} e {} é {}.' .format(a, b, a*b))
    elif opcao==3:
        if a>b:
            print('{} é maior que {}.' .format(a, b))
        elif a<b:
            print('{} é maior que {}.'.format(b, a))
        else:
            print('O número são de igual valor')
    elif opcao==4:
        a = (float(input('Digite um número: ')))
        b = (float(input('Digite um número: ')))
    else:
        print('Opção inválida. Escolha novamente.')

