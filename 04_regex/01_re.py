import re

pattern = "Hola"

text = "Hola mundo"

result = re.search(pattern, text)

if result:
  print("Se encontro")
else:
  print("No se encontro")

print(result.group())

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"

result = re.search(pattern, text)

print(result.start())
print(result.end())


### Encontrar todas las coincidencias de un patrón
# .findall() devuelve una lista con todas las coincidencias

text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"

result = re.findall(pattern, text)

print(result)
print(len(result))

result_matches = re.finditer(pattern, text)

for match in result_matches:
  print(match.group(), match.start(), match.end())