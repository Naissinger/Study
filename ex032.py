a = int(input('Em que ano você está ? '))
c = a % 4

if c == 0:
    print('\nO ano {} é BISSEXTO!'.format(a))
else:
    print('\nO ano {} não é BISSEXTO!'.format(a))