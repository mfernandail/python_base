import os
os.system("clear")

edad = 14

print("Elese")
if(edad >= 18):
  print("Eres mayor de edad")

print("Else")
if(edad >= 18):
  print("Eres mayor de edad")
else: 
  print("Eres menor de edad")

print("Else if")
if(edad >= 18):
  print("Eres mayor de edad")
elif(edad >= 13):
  print("Eres un adolescente")
else: 
  print("Eres un niño")


# Operadores lógicos
print("Operadores lógicos")
if(edad >= 18 and edad < 65):
  print("Eres un adulto")
elif(edad >= 65):
  print("Eres un adulto mayor")
else:
  print("Eres un niño o adolescente")

#Listado de operadores lógicos
# and: Devuelve True si ambas condiciones son verdaderas
# or: Devuelve True si al menos una de las condiciones es verdadera
# not: Devuelve True si la condición es falsa


# Ternario
# [Codigo que si cumple la condición] if [condición] else [código si no se cumple la condición]
print("Ternario")
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)