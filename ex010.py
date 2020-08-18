# Considerando a seguinte cotação: US$1,00 = R$3,27

dinheiro = float(input('Quanto dinheiro você tem na carteira ? R$'))
conversao = dinheiro / 3.27

print('Com R${} você pode comprar US${:.2f}'.format(dinheiro, conversao))
