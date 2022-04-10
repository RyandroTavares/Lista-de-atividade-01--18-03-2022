# 09 Faça um Programa que leia dois números inteiros e mostre o maior deles

numero1 = int(input('Digite um valor 1: '))
numero2 = int(input('Digite um valor 2: '))
print()

if numero1 > numero2:
  print('{} é maior que {}'.format(numero1, numero2))

else:
  print('{} é maior que {}'.format(numero2, numero1))