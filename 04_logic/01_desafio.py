"""
¿Está en Equilibrio la Alianza entre Reed Richards y Johnny Storm?

En el universo de los 4 Fantásticos, la unión y el equilibrio entre los poderes es fundamental para enfrentar cualquier desafío. En este problema, nos centraremos en dos de sus miembros:

Reed Richards (Mr. Fantastic), representado por la letra R.
Johnny Storm (La Antorcha Humana), representado por la letra J.

Objetivo:

Crea una función en Python que reciba una cadena de texto. Esta función debe contar cuántas veces aparece la letra R (para Reed Richards) y cuántas veces aparece la letra J (para Johnny Storm) en la cadena.

- Si la cantidad de R y la cantidad de J son iguales, se considera que la alianza entre la mente y el fuego está en equilibrio y la función debe retornar True.
- Si las cantidades no son iguales, la función debe retornar False.
- En el caso de que no aparezca ninguna de las dos letras en la cadena, se entiende que el equilibrio se mantiene (0 = 0), por lo que la función debe retornar True.
"""

# Mi version

def fantastic_four(cadena):
  count_j = 0
  count_r = 0

  cadena_lower = cadena.lower()
  
  for caracter in cadena_lower:
    if caracter == "j":
      count_j += 1
    elif caracter == "r":
      count_r += 1
  
  print(f"R = {count_r} - J = {count_j}")

  if count_j == count_r:
    return True
  else:
    return False
    

resultado = fantastic_four("Rrr JjJ hola mundo jaja")
print(f"Resultado: {resultado}")

# Mejorada
print("\n ----------------")
print("\n ----------------")

def fantastic_four_two(cadena):
  cadena = cadena.lower()
  count_j = cadena.count("j")
  count_r = cadena.count("r")

  print(f"J = {count_j} - R = {count_r}")
  return count_j == count_r

print(fantastic_four_two("JjJJj RrrRr"))

"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""
print("\n ----------------")
print("\n ----------------")

huevos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def h_carnivoros(huevos_din):
  suma = 0

  for huevo_din in huevos_din:
    if huevo_din % 2 == 0:
      suma += huevo_din
  return suma

print(h_carnivoros(huevos))