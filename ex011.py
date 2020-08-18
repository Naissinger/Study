largura = float(input('Qual a largura da parede em metros: '))
altura = float(input('Qual a altura da parede em metros: '))
tinta = (largura * altura) / 2
print('Sua parede tem a dimensão de {:.2f}m x {:.2f}m e sua área é de {:.2f}m²'.format(largura, altura, largura*altura))
print('Serão necessários {:.2f}L de tinta para pintar esta parede.'.format(tinta))