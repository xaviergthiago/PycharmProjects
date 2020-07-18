a=(int(input('Digite o valor do primeiro lado: ')))
b=(int(input('Digite o valor do segundo lado: ')))
c=(int(input('Digite o valor do terceiro lado: ')))

if ((a+b>c) and (a+c>b) and (b+c>a)):
    print('Podem formar um triângulo :D')

    if (a == b) and (b == c):
        print('Triângulo equilátero')

    elif ((a != b) and (a != c) and (b != c)):
        print('Triângulo escaleno')

    else:
        print('Triângulo isósceles')

else:
    print('Não podem formar um triângulo =/')

