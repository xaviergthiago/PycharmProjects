maior=0
menor=500
for c in range(0, 5):
    peso=(float(input("Digite o {}o peso: " .format(c+1))))
    if peso>maior:
        maior=peso
    elif peso<menor:
        menor=peso
print("O maior peso é {} Kg e o menor peso é {} Kg" .format(maior,menor))
