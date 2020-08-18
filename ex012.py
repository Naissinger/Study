produto_preço = float(input('Qual é o preço do produto ? R$'))
desconto = 5 * produto_preço / 100
produto_final = produto_preço - desconto

print('O preço final do produto com um desconto de 5% ficará {:.2f}'.format(produto_final))