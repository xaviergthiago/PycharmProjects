n1=(float(input('Digite a primeira nota: ')))
n2=(float(input('Digite a segunda nota: ')))
media=(n1+n2)/2
print('Sua média é: {} ' .format(media) )
if media<5.0:
    print('Reprovado')
elif (media>=5.0) & (media<=6.9):
    print('Recuperação')
else:
    print('Aprovado')