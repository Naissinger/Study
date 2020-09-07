import random

a1 = input('Primeiro Aluno: ')
a2 = input('Segundo Aluno: ')
a3 = input('Terceiro Aluno: ')
a4 = input('Quarto Aluno: ')
ordem = random.sample([a1, a2, a3, a4], k=4)

print('A ordem de apresentação será: {}'.format(ordem))
