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
  

def ver_opciones():
  print("\n\n===== OPCIONES =====")
  print("1. Agregar gasto")
  print("2. Ver todos los gastos")
  print("3. Ver total gastado")
  print("4. Ver gastos por categoría")
  print("5. Salir")


while True:
  ver_opciones()

  opcion_ingresada = validar_numero("Ingresa una opción: ")

  if opcion_ingresada is not opciones:
    print("Opción seleccionada fuera de rango")

  if opcion_ingresada == 5:
    break

  print(f"El numero es: {opcion_ingresada}")