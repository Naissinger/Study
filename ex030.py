n = int(input('Digite um número: '))
r = n % 2

if r == 0:
    print('\nO seu número {} é par!'.format(n))
else:
    print('\nO seu número {} é ímpar!'.format(n))