from os import system
if system("clear") != 0: system("cls")


#Dado tres números, devuelve el mayor de los tres.

a, b, c = 4, 7, 2

def mayor(a, b, c):
  
  if a > b and a > c:
    return a
  elif b > a and b > c:
    return b
  else:
    return c



print("\nResultados ejercicio 1: ")
print(mayor(a, b, c))
