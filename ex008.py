m = int(input('Informe a distância em metros: '))

print('\nA medida de {:.1f}m corresponde à: '.format(m))
print('\nQuilômetro: {}Km'.format(m/1000))
print('Hectômetro: {}Hm'.format(m/100))
print('Decâmetro:  {}Dam'.format(m/10))
print('Decímetro:  {}Dm'.format(m*10))
print('Centímetro: {}Cm'.format(m*100))
print('Milímetros: {}Mm'.format(m*1000))

