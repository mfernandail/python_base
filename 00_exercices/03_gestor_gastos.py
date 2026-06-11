import json

opciones = {
  1: "Agregar gasto",
  2: "Ver todos los gastos",
  3: "Ver total gastado",
  4: "Ver gastos por categoría",
  5: "Salir"
}

try:
  with open("./00_exercices/json/gastos_operaciones.json", "r") as gastos_guardados:
    gastos = json.load(gastos_guardados)
except FileNotFoundError:
  gastos = []

def validar_numero(input_ingresado, num_min = 0):
  while True:
    try:
      numero = int(input((input_ingresado)))
      
      if numero >= num_min:
        return numero
      else:
        print("Debe ser número ser mayor")

    except:
      print("Debe ser número entero")

def validar_vacios(input_ingresado):
  while True:
    texto = input(input_ingresado)

    if len(texto) > 0:
      return texto
    else:
      print("Por favor ingresa algun texto")


def agregar_gasto():
  while True:
    gasto_nuevo_desc = validar_vacios("Ingrese la descripción del gasto: ")
    gasto_nuevo_monto = validar_numero("Ingrese el monto del gasto: $")
    gasto_nuevo_cat = validar_vacios("Ingrese la categoria del gasto: ")

    print(f"\n{gasto_nuevo_desc}")
    print(f"\n{gasto_nuevo_monto}")
    print(f"\n{gasto_nuevo_cat}")


def ver_opciones():
  print("\n\n===== OPCIONES =====")
  print("1. Agregar gasto")
  print("2. Ver todos los gastos")
  print("3. Ver total gastado")
  print("4. Ver gastos por categoría")
  print("5. Salir")



while True:
  ver_opciones()

  opcion_ingresada = validar_numero("\nIngresa una opción: ")

  if opcion_ingresada not in opciones:
    print("Opción seleccionada fuera de rango")
    continue
  
  print("\n= = = = = = = = = = = = = = = = = = = = = = = =")
  print(f"Opción seleccionada: {opciones[opcion_ingresada]}")
  print("= = = = = = = = = = = = = = = = = = = = = = = =\n")

  if opcion_ingresada == 1:
    agregar_gasto()

  elif opcion_ingresada == 5:
    break
