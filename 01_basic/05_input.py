nombre = input("Hola, ¿cómo te llamas?\n")
print(f"Hola {nombre}, encantado de conocerte")

# Ten en cuenta que la función input() devuelve un string
# Así que si queremos obtener un número se debe convertir el string a un número
age = input("¿Cuántos años tienes?\n")
age = int(age)
print(f"Tienes {age} años")

# La función input() también puede devolver múltiples valores
# Para hacerlo, el usuario debe separar los valores con una coma
print("Obtener múltiples valores a la vez")
country, city = input("¿En qué país y ciudad vives?\n").split()

print(f"Vives en {country}, {city}")