v = input('Digite algo: ')

print('\nO tipo primitivo desse valor é: ', type(v))
print('Só tem espaços ?', v.isspace())
print('É um número ?', v.isnumeric())
print('É um alfabético ?', v.isalpha())
print('É um alfanumérico ?', v.isalnum())
print('Está em maiúsculas ?', v.isupper())
print('Está em minúsculas ?', v.islower())
print('Está capitalizada ?', v.istitle())

