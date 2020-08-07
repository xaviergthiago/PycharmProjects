primeiroTermo=(int(input('Digite o primeiro termo da P.A.: ')))
razao=(int(input('Digite a razão da P.A.: ')))
decimo=int(primeiroTermo+9*razao)
termo=primeiroTermo
while termo<=decimo:
    print(termo, end=' ')
    termo=termo+razao