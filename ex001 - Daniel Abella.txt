# 01 Realiza a leitura de 2 floats e imprime as seguintes operações: soma, subtração, multiplicação, divisão e resto da divisão.

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite um número: '))
print()

print('A soma é {}'.format(numero1 + numero2))
print('A subtração é {}'.format(numero1 - numero2))
print('A multiplicação é {}'.format(numero1 * numero2))
print('A divisão é {:.2f}'.format(numero1 / numero2))
print('O resto da divisão é {}'.format(numero1 % numero2))
