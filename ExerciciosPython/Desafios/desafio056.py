vinte=0
idadevelho=0
media=0

for c in range (0,4):
    nome=(input("Digite o nome: "))
    idade=(int(input("Digite a idade: ")))
    media=media+idade
    sexo = (int(input("Escolha o sexo: [1] Feminino | [2] Masculino ")))

    if (idade<20) and (sexo==1):
        vinte=vinte+1

    if (idade>idadevelho) and (sexo==2):
        idadevelho=idade
        nomevelho=nome

print("A média de idade do grupo é de {} anos" .format(media/4))
print("Há um total de {} mulheres com menos de 20 anos" .format(vinte))
print("O homem mais velho tem {} anos e se chama {}" .format(idadevelho, nomevelho))