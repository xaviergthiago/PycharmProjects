primeiroTermo=(int(input('Digite o primeiro termo da P.A.: ')))
razao=(int(input('Digite a razão da P.A.: ')))
#decimo=primeiroTermo+(10-1)*razao
decimo=primeiroTermo+9*razao
for c in range(primeiroTermo, decimo, razao):
    print(c, end=' ')