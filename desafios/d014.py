from math import hypot

n1 = float(input('Digite um valor de um cateto: '))
n2 = float(input('Digite o segundo valor de um cateto: '))
hip = hypot(n1, n2)

print('A hipoternusa é {:.2f}'.format(hip))
