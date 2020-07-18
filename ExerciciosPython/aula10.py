'''tempo=int(input('Quantos anos seu carro tem? '))
if tempo<=3:
    print('Carro novo')
else:
    print ('Carro velho')

print ('Carro novo' if tempo<=3 else 'Carro velho')'''

'''nome=str(input('Qual seu nome? '))
if nome=='Thiago':
    print('Que nome lindo você tem!')
else:
    print('Queria que fosse Thiago XD')
print('Bom dia, {} ' .format(nome))'''

n1=(float(input('Digite a primeira nota ')))
n2=(float(input('Digite a segunda nota ')))
media=(n1+n2)/2
print('Sua média foi {} ' .format(media))
if media >=6.0:
    print('Aprovado')
else:
    print('Reprovado, filho da puta! Se fudeu!')