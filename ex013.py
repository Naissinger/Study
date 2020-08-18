salario = float(input('Qual o salário do Funcionário : R$'))
aumento = 15 * salario / 100
resultado = salario + aumento

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(salario, resultado))