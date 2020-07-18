import math
num = float(input("Digite um número "))
arredondabaixo=math.floor(num)
arredondacima=math.ceil(num)
print ("O número inteiro arredondado pra cima é {} e arredondado pra baixo é {} " .format (arredondacima, arredondabaixo))