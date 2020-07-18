numero=(int(input('Digite um número inteiro: ')))
opcao=(int(input('Selecione: 1-para binário, 2-para octal, 3-para hexadecimal ')))
if opcao==1:
    print('Em binário o número {} é: {} ' .format(numero, bin(numero)[2:])) # [2:] para tratamento de String, pois Python imprime 0b antes do valor convertido
elif opcao==2:
    print('Em octal o número {} é: {} ' .format(numero, oct(numero)[2:])) # [2:] para tratamento de String, pois Python imprime 0o antes do valor convertido
elif opcao==3:
    print('Em hexadecimal o número {} é: {} ' .format(numero, hex(numero)[2:])) # [2:] para tratamento de String, pois Python imprime 0x antes do valor convertido
else:
    print('Opção inválida!')