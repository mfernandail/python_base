import re

text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = r"H.la" 

found = re.findall(pattern, text)
print(found)

text = "Hola mundo. Hello word."
pattern = r"\."

found = re.findall(pattern, text)
print(found)

text = "Mi numero de telefono es 123456789"
pattern = r'\d{9}'

found = re.findall(pattern, text)
print(found)

print("Numero")
text = "+56 944848489"
pattern = r'^\+\d{1,3} '
found = re.search(pattern, text)
if found: print(f"Se encontró un número {found.group()}")

text = "cadena de texto que termine en: mundo"
pattern = r"mundo$"

valid = re.search(pattern, text)
if valid: print("La cedena es valida", valid)
else: print("La cadena no es valida, no termina en mundo")

text = "micorreo@gmail.com"
pattern = r"^\w+@gmail\.com$"

valid = re.search(pattern, text)

print(text, pattern, valid)

if valid: print("El correo es valido")
else: print("El correo no es valido ", text, valid)

# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.pdf midu-of.webp secret.txt"
pattern = r"\w+\.txt"

found = re.findall(pattern, files)
print(found)