#import math
from math import hypot
c1=float(input("Digite o valor do primeiro cateto "))
c2=float(input("Digite o valor do segundo cateto "))
'''h=((pow(c1,2))+(pow(c2,2)))**0.5
print ("A hipotenusa vale {:.2f}" .format(h))'''
#h = math.hypot(c1, c2)
h = hypot(c1, c2)
print ("A hipotenusa vale {}" .format(h))