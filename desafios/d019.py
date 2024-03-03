nome = str(input('Digite o seu nome completo: ')).strip()
nomemax = nome.upper()
nomemin = nome.lower()
nometam = len(nome)-nome.count(' ') # quantas letras tem, sem contar os espaços
primeiro = nome.find(' ') # quantas letras tem o primeiro nome
separa = nome.split()


print("Seu nome em letra maiúscula é: {}".format(nomemax))
print('Seu nome em letra minuscula é: {}'.format(nomemin))
print('Seu nome tem {} letras'.format(nometam))
print('Seu primeiro nome tem {} letras'.format(primeiro))
print('Seu primeiro nome é {}'.format(separa[0]))


