nome=input('Digite seu nome ')
print('O nome é: {} ' .format(nome))
print('Maiúscula: {} ' .format(nome.upper()))
print('Minuscula: {} ' .format(nome.lower()))
print('Quantidade total de letras com espaço: {} ' .format(len(nome.strip())))
dividido=nome.split()
soma=(dividido[0]+dividido[1]+dividido[2])
print('Quantidade total de letras sem espaço: {} ' .format(len(soma)))
print('Quantidade de letras do primeiro nome: {} ' .format(len(dividido[0])))