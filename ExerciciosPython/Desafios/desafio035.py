a=(int(input('Digite o valor do primeiro lado: ')))
b=(int(input('Digite o valor do segundo lado: ')))
c=(int(input('Digite o valor do terceiro lado: ')))

if ((a+b>c) and (a+c>b) and (b+c>a)):
    print('Podem formar um triângulo :D')
else:
    print('Não podem formar um triângulo =/')