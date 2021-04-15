# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a seis;
# A mensagem "Reprovado", se a média for menor do que seis;
# A mensagem "Aprovado com Honra", se a média for igual a dez.

nota1 = float(input("Digite o valor da primeira nota: \n"))
nota2 = float(input("Digite o valor da segunda nota: \n"))

media = (nota1 + nota2) / 2

if media == 10:
  print("Aluno aprovado com honras")
elif media >= 6:
  print("Aluno Aprovado {:.2f}".format(media))
else:
  print("Aluno Reprovado {:.2f}".format(media))    