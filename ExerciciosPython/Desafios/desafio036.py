valor=(float(input('Qual o valor da casa? ')))
salario=(float(input('Qual o salário do comprador? ')))
tempo=(int(input('Em quantos anos vai pagar? ')))
tempo=tempo*12
prestacao=valor/tempo
if prestacao>0.3*salario:
    print('O empréstimo foi negado')
else:
    print('Empréstimo aprovado')
print('O valor mínimo da prestação é de {:.2f}' .format(0.3*salario))
print('Para comprar uma casa de R$ {:.2f} em {} prestações cada prestação terá o valor de {:.2f}' .format(valor, tempo, prestacao))