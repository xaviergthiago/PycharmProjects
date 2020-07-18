velocidade=(float(input('Digite a velocidade: ')))
if velocidade <=80:
    print('A velocidade está dentro do limite aceitável: {} km/h ' .format(velocidade))
else:
    print('Você ultrapassou o limite de 80 km/h, sua velocidade foi de {} km/h e sua multa é no valor de {:3} reais ' .format(velocidade, 7*velocidade-560))