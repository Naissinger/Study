import math

angulo = int(input('Digite o ângulo que você deseja: '))
radiano = math.radians(angulo)

print('\nO ângulo de {} tem o SENO de {:.2f}'.format(angulo, math.sin(radiano)))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, math.cos(radiano)))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, math.tan(radiano)))
