print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('----------Analisador de Triângulos----------')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
c = s1+s2

if c > s3:
    print('\nOs segmentos acima PODEM FORMAR um triângulo!')
else:
    print('\nOs segmentos acima NÃO PODEM FORMAR um triângulo!')
