multiplicando=(int(input('Digite um número para ver sua tabuada: ')))
for multiplicador in range(0, 11):
    print('{} × {:2} = {:3}' .format(multiplicando, multiplicador, multiplicador*multiplicando))