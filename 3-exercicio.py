#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

gender = input("Digite a inicial do seu gênero: \n")

if gender == "f" or gender == "F":
  print("Gênero Feminino")
elif gender == "m" or gender == "M":
  print("Gênero Masculino")
else:
  print("Gênero Inválido")  