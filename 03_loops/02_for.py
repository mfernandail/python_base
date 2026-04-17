print(f"For")

numeros = [1,2,3,4,5]

for numero in numeros:
  print(f"Numero: ", numero)

print(f"\nenumerate:")
for index, numero in enumerate(numeros):
  print(f"En el index: {index} esta el numero: {numero}")

print(f"\nBreak:")

for numero in numeros:
  print(f"Numero: {numero}")
  if(numero == 3):
    break

print(f"\nContinue:")

for numero in numeros:
  if(numero % 2 == 0):
    continue
  print(f"Numero: {numero}")



print(f"\nList comprehension")
animales = ["perro", "gato", "foca", "hormiga", "elefante", "huemul"]

animal_upper = [animal.upper() for animal in animales]
print(animal_upper)

print("\nEjercicio")
numPares = [num for num in [1,2,3,4,5,6] if(num % 2 == 0)]
print(numPares)