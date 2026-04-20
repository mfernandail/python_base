import os
os.system("clear")

contador = 6
while contador > 0:
  print(contador)
  contador -= 1

while True:
  print("Esto se ejecutará infinitamente")
  contador += 1
  if contador > 10:
    break

# continue
print("\ncontinue")
contador = 0
while contador < 10:
  contador += 1
  if contador % 2 == 0:
    continue
  print(contador)

# else
print("===============================")
print("else")
print("===============================")
contador = 0
while contador < 5:
  print(contador)
  contador += 1
else:
  print("El contador ha llegado a 5")

print("===============================")
print("else break")
print("===============================")
contador = 0
while contador < 5:
  print(contador)
  contador += 1
  break
else:
  print("El contador ha llegado a 5")





numero = -1

while numero < 0:
  try:
    numero = int(input("Ingrese un número positivo: "))
    if numero < 0:
      print("Número inválido. Intente nuevamente.")
  except ValueError:
    print("Entrada no válida. Por favor, ingrese un número entero.")
print(f"El numero es {numero}")