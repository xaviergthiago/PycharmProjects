soma=0

'''for c in range(1, 501, 2):
    if c%3==0:
        soma=soma+c
print('A soma dos número ímpares múltiplos de 3 entre 1 e 500 é: {} ' .format(soma))''' # várias formas de se fazer

for c in range(3, 501, 6):
    soma = soma + c
print('A soma dos número ímpares múltiplos de 3 entre 1 e 500 é: {} ' .format(soma))