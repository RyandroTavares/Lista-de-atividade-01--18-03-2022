# 05 Realiza a leitura de 1 float referente ao valor de um produto e imprime o valor com descontos de 10%, 20% e 50%.

produto = float(input('Digite o valor do produto: R$ '))
des10 = (produto*10) / 100
des10 = produto - des10
print()

print('O produto com 10% de desconto R$ {}'.format(des10))
print()

des20 = (produto*20) / 100
des20 = produto - des20
print('O produto com 20% de desconto R$ {}'.format(des20))
print()

des50 = (produto*50) / 100
des50 = produto - des50
print('O produto com 50% de desconto R$ {}'.format(des50))
