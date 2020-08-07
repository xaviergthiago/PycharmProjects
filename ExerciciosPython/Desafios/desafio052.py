numero=(int(input("Digite um número: ")))
primo=0
for c in range(1, numero):
    if numero % c == 0:
        primo=primo+1

if primo < 2:
    print("O número {} é primo. " .format(numero))
else:
    print("O número {} NÃO é primo. ".format(numero))