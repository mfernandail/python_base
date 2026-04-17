# Range no crea un lista, el tipo es Range
# Range es un objeto iterable, no una lista. Se puede convertir a lista con list(range(5))
# Range es eficiente en memoria, ya que no almacena todos los números en memoria, sino que los genera sobre la marcha.
print("\nRange")

nums = range(5)

print(nums)

for num in range(10):
  print(num)

print("\nRange con rango:")
for num in range(6, 12):
  print(num)

print("\nRange con rango, pasos:")
for num in range(3, 12, 2):
  print(num)


print("\nRange numeros negativos:")
for num in range(-10, 0):
  print(num)


print("\nRange numeros decrementando:")
for num in range(10, 0, -1):
  print(num)

print("\nCrear la lista con un range")
nums = range(10)
list_of_nums = list(nums)

print(type(list_of_nums))

print("\nContador")
for _ in range(5):
  print("5 Veces algo sin necesidad de crear una variable")
