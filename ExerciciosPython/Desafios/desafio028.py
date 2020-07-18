'''from random import shuffle
numero=(input('Digite um número de 1 a 5 '))
print('O número que você digitou é {} ' .format(numero))
lista=['1', '2', '3', '4', '5']
shuffle(lista)
if numero==lista[0]:
    print('ACERTOU!')
else:
    print('ERROU')
print('O número sorteado foi {} ' .format(lista[0]))'''

from random import shuffle
numero=(int(input('Digite um número de 1 a 5 ')))
print('O número que você digitou é {} ' .format(numero))
lista=[1, 2, 3, 4, 5]
shuffle(lista)
if numero==lista[0]:
    print('ACERTOU!')
else:
    print('ERROU')
print('O número sorteado foi {} ' .format(lista[0]))





