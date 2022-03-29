# 06 Realiza a leitura de 1 float referente ao salário do cidadão e apresenta o salário com reajuste de 10% da inflação.

salario = float(input('Digite o salário: R$ '))
infla10 = (salario*10) / 100
infla10 = salario + infla10
print()

print('O seu salário com 10% de inflação R$ {}'.format(infla10))