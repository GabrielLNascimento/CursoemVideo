import math

n1 = float(input('Digite um valor de um cateto: '))
n2 = float(input('Digite o segundo valor de um cateto: '))

hip = (pow(n1,2) + pow(n2,2))
fim = math.sqrt(hip)
print('A hipoternusa é {}'.format(fim))
