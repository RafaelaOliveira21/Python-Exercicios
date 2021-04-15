#Faça um Programa que peça dois números e imprima o maior deles.

primeiroNumero = float(input("Digite um número: \n"))
segundoNumero = float(input("Digite outro numero: \n"))

if primeiroNumero > segundoNumero:
  print("O maior numero é: " + primeiroNumero)
elif primeiroNumero == segundoNumero:
  print("Os números são iguais: " + primeiroNumero)
else:
  print("O maior numero é: " + segundoNumero)   


