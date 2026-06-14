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

def guardar_json():
  with open("./00_exercices/json/gastos_operaciones.json", "w") as items:
    json.dump(gastos, items, indent=2)

def validar_numero(input_ingresado, num_min = 0):
  while True:
    try:
      numero = int(input((input_ingresado)))
      
      if numero >= num_min:
        return numero
      else:
        print("Debe ser número ser mayor")

    except ValueError:
      print("Debe ser número entero")

def validar_vacios(input_ingresado):
  while True:
    texto = input(input_ingresado)

    if texto:
      return texto
    else:
      print("Por favor ingresa algun texto")

def calcular_total():
  total = sum(gasto["monto"] for gasto in gastos)

  return total

def agregar_gasto():
  gasto_nuevo_desc = validar_vacios("Ingrese la descripción del gasto: ")
  gasto_nuevo_monto = validar_numero("Ingrese el monto del gasto: $")
  gasto_nuevo_cat = validar_vacios("Ingrese la categoria del gasto: ")

  gastos.append({
    "descripcion": gasto_nuevo_desc,
    "monto": gasto_nuevo_monto,
    "categoria": gasto_nuevo_cat
  })

  guardar_json()

  print(gastos)

def ver_gastos():
  if len(gastos) == 0:
    print("No hay gastos para mostrar")
    return
  
  total_gastos = calcular_total()

  for i, gasto in enumerate(gastos):
    print(f"{i + 1}. {gasto['descripcion']} - ${gasto['monto']} - {gasto['categoria']}")

  print(f"\nTotal: ${total_gastos}")

def ver_gastos_total():
  if len(gastos) == 0:
    print("No hay gastos para mostrar")
    return
  
  total_gastos = calcular_total()

  print(f"\nTotal: ${total_gastos}")

def ver_gastos_categoria():
  if len(gastos) == 0:
    print("No hay gastos para mostrar")
    return
  
  gasto_categorias = {}

  for gasto in gastos:
    categoria = gasto["categoria"]

    if categoria not in gasto_categorias:
      gasto_categorias[categoria] = 0

    gasto_categorias[categoria] += gasto["monto"]

    
  print(gasto_categorias)

def ver_opciones():
  print("\n\n===== OPCIONES =====")
  for numero, texto in opciones.items():
    print(f"{numero}. {texto}")

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
  elif opcion_ingresada == 2:
    ver_gastos()
  elif opcion_ingresada == 3:
    ver_gastos_total()
  elif opcion_ingresada == 4:
    ver_gastos_categoria()
  elif opcion_ingresada == 5:
    break
