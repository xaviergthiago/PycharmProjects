preco=(float(input('Qual o valor do produto? ')))
pagamento=(str(input('Qual a forma de pagamento? ')))

if (pagamento=='dinheiro') or (pagamento=='cheque'):
    preco=preco-(0.1*preco)
    print('Você receberá 10% de desconto e pagará R${}' .format(preco))
elif (pagamento=='cartao'):
    parcela=(int(input('Em quantas vezes deseja parcelar? ')))
    if parcela==1:
        preco=preco-(0.05*preco)
        print('Você receberá 5% de desconto e pagará R${}' .format(preco))
    elif parcela==2:
        print('Você não receberá desconto e pagará R${}'.format(preco))
    else:
        preco=preco+(0.2*preco)
        print('Você terá 20% de juros e pagará R${}'.format(preco))
else:
    print('Forma de pagamento inválida')