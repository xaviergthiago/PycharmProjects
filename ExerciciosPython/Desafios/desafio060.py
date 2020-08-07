'''numero=(int(input("Digite um número: ")))
fatorial=1
for c in range (1, numero+1):
    fatorial=fatorial*c
print('O fatorial é {}' .format(fatorial))'''

numero=(int(input("Digite um número: ")))
fatorial=1
while numero>1:
    fatorial=fatorial*numero
    numero=numero-1
print('O fatorial é {}' .format(fatorial))

