x = "awesome" # variavel global

def myfunc(z):
  print(z)
  y = "Só existe aqui dentro da função" # variavel local
  print("Python is " + x)
  print(y)

myfunc(2)