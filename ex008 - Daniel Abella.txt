# 08 Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:

# • A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; 
# • A mensagem "Reprovado", se a média for menor do que sete; 
# • A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
media = (nota1 + nota2) / 2
print()

if media >= 7 and media < 10:
  print('Aprovado! média {}'.format(media))

elif media < 7:
  print('Reprovado! média {}'.format(media))

else:
  print('Aprovado com distinção! média {}'.format(media))