velocidade=(float(input('Digite a velocidade: ')))
if velocidade<=200:
    print('Sua velocidade foi de {} e o custo foi de {} ' .format (velocidade, 0.5*velocidade))
else:
    print('Sua velocidade foi de {} e o custo foi de {} ' .format (velocidade, 0.45*velocidade))
