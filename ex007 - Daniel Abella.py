# 07 Realiza a leitura de 1 int e apresenta se ele é par ou ímpar.

numero = int(input('Digite um valor: '))
var = numero % 2
print()

if var == 1:
  print('O número {} é impar'.format(numero))
  
else:
  print('O número {} é par'.format(numero))