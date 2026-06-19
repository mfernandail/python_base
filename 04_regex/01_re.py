import re

pattern = "Hola"

text = "Hola mundo"

result = re.search(pattern, text)

if result:
  print("Se encontro")
else:
  print("No se encontro")