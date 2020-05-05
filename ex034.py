p = float(input('Informe o seu salário: R$'))
a = (110/100)*p

if p > int('1250'):
    print('\nO seu salário teve um aumento de 10%, e ficou: R${:.2f}'.format(a))
else:
    print('\nO seu salário teve um aumento de 15%, e ficou: R${:.2f}'.format((115/100)*p))