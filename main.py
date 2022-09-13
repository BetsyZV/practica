import time

for numero_carga in range (5,0,-1):
  print (numero_carga)
  time.sleep(1)


print("\n El promedio de", a, "y", b, "es",c, "\n")
#solicitar dos numeros y la operación a realizar
a= int(input("Ingrese número: "))
b= int(input("Ingrese número: "))
c= input("Ingrese operador matemático: ")
while c not in ("+", "-", "*", "/"):
  c = input ("Debes ingresar +, -, *, /. Ingresa nuevamente un operador matemático: ")
r=0
if c == "+":
  r=a+b
  print ("\n La suma de", a, "+", b, "es:", r)

elif c == "-":
  r=a-b
  print ("\n La resta de", a, "-", b, "es:", r)

elif c == "*":
  r=a*b
  print ("\n La multiplicación de", a, "*", b, "es:", r)

elif c == "/":
  r=a/b
  print ("\n La suma de", a, "+", b, "es:", r)

  #solicitar numero de filas e imprimir cruces
a= int(input("\nIngrese número de filas: "))
b=0
while b <= a:
  c=0
  while c < b:
    print ("+", end = " ")
    c = c + 1
  print (" ")
  b = b + 1