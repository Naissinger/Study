v = int(input('A quantos Km o carro estava ? '))
m = (v - 80)*7

if v > 80:
    print('\nEntão você foi multado! O limite de velocidade era de 80Km/h')
    print('A sua multa ficará: R${:.2f}'.format(m))
else:
    print('\nVocê estava a baixo do limite de velocidade! PARABÉNS!')

