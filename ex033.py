p1 = int(input('Digite o primeiro número: '))
p2 = int(input('Digite o segundo número: '))
p3 = int(input('Digite o terceiro número: '))
maior = p1
menor = p1

 # Achando o maior número

if (p2 > maior):
    maior = p2
if (p3 > maior):
    maior = p3

print('O maior número é: {}'.format(maior))

# Achando o menor número

if (p2 < menor):
        menor = p2
if (p3 < menor):
        menor = p3
print('O menor número é: {}'.format(menor))


