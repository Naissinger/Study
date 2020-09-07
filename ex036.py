# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você pretende pagar? '))
pmensal = casa / (anos*12)
limite = salario * 0.3

print('\nPara pagar uma casa de R${} em {} anos a prestação será de R${:.2f}'.format(casa, anos, pmensal))

if pmensal <= limite:
    print('\nParabéns o seu empréstimo foi CONCEDIDO !')
else:
    print('\nDesculpe, o seu empréstimo foi NEGADO !')
    
