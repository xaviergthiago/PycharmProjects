atual=(int(input("Digite o ano atual: ")))
maior=0
menor=0
for c in range(0,7):
    nascimento=(int(input("Digite o ano de nascimento da {}a pessoa: " .format(c+1))))

    if atual-nascimento>=21:
        maior=maior+1
    else:
        menor=menor+1

print("Total de {} COM maioridade atinginda" .format(maior))
print("Total de {} SEM maioridade atinginda" .format(menor))