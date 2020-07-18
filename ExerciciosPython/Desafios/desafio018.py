#import math
from math import radians, sin, cos, tan
a=float(input("Digite um ângulo em graus: "))
'''a=math.radians(a) #converte para radianos o valor digitado
cos=math.cos(a)
sen=math.sin(a)
tg=math.tan(a)'''
a=radians(a) #converte para radianos o valor digitado
sen=sin(a)
cos=cos(a)
tg=tan(a)
print ("O seno é {:.2}, o cosseno é {:.2} e a tangente é {:.2}" .format(sen, cos, tg))