nome=str(input('Qual seu nome? '))
if nome=='Thiago':
    print('Que nome esplêndido!')
elif nome=='Pedro' or nome=='Maria' or nome=='Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é comum!')
print('Tenha um bom dia, {}! ' .format(nome))