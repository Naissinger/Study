# Sabe-se que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram rodados? '))
total = (dias * 60) + (km * 0.15)

print('\nO total a pagar pelo aluguel do carro é de R${}'.format(total))
