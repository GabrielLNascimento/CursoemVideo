from math import sin, tan, cos, radians
ang = float(input('Digite um ângulo: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O seno é: {:.2f}'.format(seno))
print('O cosseno é: {:.2f}'.format(cos))
print('A tangente é: {:.2f}'.format(tan))