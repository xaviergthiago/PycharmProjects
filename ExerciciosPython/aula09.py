frase='Curso em Vídeo Python'
print (frase[3])
print (frase[3:13])
print (frase[3:])
print(frase[:13])
print(frase[3:13:2])
print(frase[:2])

print("""I keep on reaching and I, keep on trying
But you never even hold me and it seems like you don't know me baby
I keep on yearning and I, I guess I'm learning
That it's just a losing fight 'cause there's no passion in your eyes
No, no, no, no, babe""")

print(frase.count('o', 2, 13))
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O', 2, 15))
print(len(frase))
print(frase.replace('Python', 'Android')) #Usa-se replace pois não é possivel aribuir valor a posições, como em vetores
print('Curso' in frase)
print('curso' in frase)
print('CURSO' in frase.upper())
print(frase.find('CURSO'))
print(frase.find('urso')) #Onde inicia o trecho "urso"
print(frase.lower().find('vídeo'))
print(frase.lower().find('video')) #sem acento

print(frase.split())
dividido=frase.split()
print(dividido[2])
print(dividido[2][3])
print ('-'.join(dividido)) #semelhança na saída
print ('-'.join(frase.split())) #semelhança na saída

frase = '   Aprenda Python   '
print(frase) #diferença na saída
print(frase.strip()) #diferença na saída
print(frase.rstrip())
print(frase.lstrip())
print(frase.strip().split())
dividido=frase.strip().split()
print(dividido[0] + dividido[1]) #semelhança na saída
print ('{}{}' .format(dividido[0], dividido[1])) #semelhança na saída