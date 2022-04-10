# 12 Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos deve obedecer à tabela acima.

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
media = (nota1 + nota2) / 2
print()

if media > 9 and media <= 10:
  print('Nota A, média {}'.format(media))

elif media > 7.5 and media <= 9:
  print('Nota B, média {}'.format(media))

elif media > 6 and media <= 7.5:
  print('Nota C, média {}'.format(media))

elif media > 4 and media <= 6:
  print('Nota D, média {}'.format(media))

else:
  print('Nota E, média {}'.format(media))