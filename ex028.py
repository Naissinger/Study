import random

n = random.randint(1, 5)
p = int(input('Chute um número de 1 a 5: '))

if p == n:
    print('Você acertou! PARABÉNS!')
else:
    print('Você errou! TENTE MAIS TARDE!')