#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

number = int(input("Digite um numero: \n"))

if number > 0:
  print("Numero Positivo")
elif number == 0:
  print("Numero Neutro")
else:
  print("Numero Negativo")  