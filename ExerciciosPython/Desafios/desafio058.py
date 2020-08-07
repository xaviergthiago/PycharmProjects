from random import shuffle
tentativa=0
numero=int
lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(lista)
#print(lista) #chamada pra confirmar se a lista estava sendo embaralhada

while numero!=lista[0]:

    numero = (int(input('Digite um número de 0 a 10 ')))
    print('O número que você digitou é {} '.format(numero))
    #print('O número sorteado foi {}'.format(lista[0]))

    if numero!=lista[0]:
        print('ERROU!')
    else:
        print('ACERTOU!')

    tentativa=tentativa+1

print('O jogador tentou {} vezes até acertar.' .format(tentativa))