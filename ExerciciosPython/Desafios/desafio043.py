altura=(float(input('Digite sua altura: ')))
peso=(float(input('Digite seu peso: ')))
IMC=peso/altura**2
print('Seu IMC é: {:.2f}' .format(IMC))
if IMC<18.5:
    print('Abaixo do peso')
elif (IMC>=18.5) & (IMC<25):
    print('Peso ideal')
elif (IMC>=25) & (IMC<30):
    print('Sobrepeso')
elif(IMC>=30) & (IMC<=40):
    print('Obesidade')
elif(IMC>40):
    print('Obesidade mórbida')