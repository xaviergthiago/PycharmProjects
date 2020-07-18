idade=(int(input('Digite a idade: ')))
if idade<=9:
    print('A categoria é MIRIM')
elif (idade>9) & (idade<=14):
    print('A categoria é INFANTIL')
elif (idade>14) & (idade<=19):
    print('A categoria é JUNIOR')
elif (idade>19) & (idade<=20):
    print('A categoria é SÊNIOR')
else:
    print('A categoria é MASTER')