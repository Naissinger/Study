import random

a1 = input('Primeiro Aluno: ')
a2 = input('Segundo Aluno: ')
a3 = input('Terceiro Aluno: ')
a4 = input('Quarto Aluno: ')


print('\nO Aluno escolhido foi {}'.format(random.choice([a1, a2, a3, a4])))
