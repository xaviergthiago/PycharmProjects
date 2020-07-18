ano=(int(input('Digite seu ano de nascimento: ')))
atual=int(input('Digite o ano atual: '))
if (atual-ano)<18:
    print('Você ainda vai se alistar e deverá ser daqui a {} anos.' .format(18-(atual-ano)))
elif(atual-ano)==18:
    print('Você deve se alistar esse ano.')
else:
    print('Você deveria ter se alistado há {} anos' .format((atual-ano)-18))