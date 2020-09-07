import math

coposto = float(input('Comprimento do cateto oposto: '))
cadjacente = float(input('Comprimento do cateto oposto: '))
h = math.hypot(coposto, cadjacente)

print('\nA hipotenusa vai medir {:.2f}'.format(h))
