# 11 As Organizações Hamurabi Medeiros resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.

# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# • salários até R$ 280,00 (incluindo) : aumento de 20%
# • salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# • salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# • salários de R$ 1500,00 em diante : aumento de 5%

salario = float(input('Digite o seu salário: '))
des = 0
print()

if salario <= 280:
  des = 20

elif salario > 280 and salario <= 700:
  des = 15

elif salario > 700 and salario < 1500:
  des = 10

else:
  des = 5

desco = (salario*des) / 100
desc = salario + desco

print('O salário antes do reajuste: R$ {} \nO percentual do aumento aplicado: {}% \nO valor do aumento: R$ {} \nO novo salário, após o aumento: R$ {}'.format(salario, des, desco, desc))