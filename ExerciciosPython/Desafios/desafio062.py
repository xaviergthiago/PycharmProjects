primeiroTermo=(int(input('Digite o primeiro termo da P.A.: ')))
razao=(int(input('Digite a razão da P.A.: ')))
decimo=primeiroTermo+9*razao
termo=primeiroTermo
opcao=1

while opcao!=0:
    while termo<=decimo:
        print(termo, end=' ')
        termo=termo+razao

    opcao=(int(input('Deseja mostrar mais quantos termos? ')))
    enezimo=decimo+opcao*razao
    while termo<=enezimo:
        print(termo, end=' ')
        termo=termo+razao

