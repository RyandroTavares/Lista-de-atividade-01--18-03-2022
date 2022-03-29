# 10 Faça um programa que pede dois inteiro e armazene em duas variáveis. Em seguida, troque o valor das variáveis e exiba na tela

# Exemplo:
# var1 = 1
# var2 = 2

# var3 = var1 'Ou seja var3 se torna o valor de var1 = 1'
# var1 continua com valor 1

# var1 = var2 'Ou seja var1 se torna o valor de var2 = 2'
# var1 remove o valor de 1 e passa a ser com valor de 2

# var2 = var3 'Ou seja var2 passa a ser com valor de 1'

# Resultado
# Var1 = 2
# Var2 = 1
# Var3 = 1

var1 = int(input('Digite um número: '))
var2 = int(input('Digite outro número: '))
print()

var3 = var1
var1 = var2
var2 = var3

print(var1)
print(var2)