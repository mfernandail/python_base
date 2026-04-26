# Los dictionarios son colecciones de pares clave-valor. Son mutables y no ordenados (hasta Python 3.6, a partir de Python 3.7 mantienen el orden de inserción). Se definen con llaves {} y los pares clave-valor se separan por comas. Las claves deben ser únicas e inmutables (como strings, números o tuplas), mientras que los valores pueden ser de cualquier tipo.
print("\nDictionaries")

# Crear un diccionario
persona = {
  "nombre": "Maria",
  "edad": 30,
  "telefono": "123-456-7890",
  "comida_favorita": ["Pizza", "Sushi", "Tacos"],
  "direccion": {
    "calle": "123 Main St",
    "ciudad": "Arica",
    "pais": "Chile"
  }
}
print(persona)
# Acceder a los valores
print(persona["nombre"])  # Maria
print(persona["edad"])  # 30
print(persona["comida_favorita"])  # ['Pizza', 'Sushi', 'Tacos']
print(persona["direccion"]["ciudad"])  # Arica
print(persona.get("nombre"))  # Maria
print(persona.get("telefono", "No disponible"))  # No disponible
print(persona["comida_favorita"][1])

# Eliminar un elemento del diccionario

del persona["telefono"]

edad_persona = persona.pop("edad", None)
print(f"Edad eliminada: {edad_persona}")

print(persona)

# Sobre escribir un valor existente
persona_a = {
  "nombre": "Fernanda",
  "edad": 37,
  "telefono": "123-456-7890"
}

persona_b = {
  "nombre": "Juan",
  "edad": 24,
  "telefono": "223-456-4433"
}

print("\nPersona A:", persona_a)
print("Persona B:", persona_b)  

persona_a.update(persona_b)
print("\nPersona A después de update:", persona_a)
print("Persona B después de update:", persona_b)