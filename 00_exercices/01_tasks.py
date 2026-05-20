import json

try:
  with open("./00_exercices/json/tareas.json", "r") as archivo:
    tareas = json.load(archivo)
except FileNotFoundError:
  tareas = []

def validar_numero(cadena, num_min = 0):
  while True:
    try:
      numero = int(input(cadena))

      if numero >= num_min:
        return numero
      else:
        print(f"\nEl número debe ser mayor o igual a {num_min}")
    except:
      print("\nSolo se admiten números")

def guardar_tareas_json():
  with open("tareas.json", "w") as archivo:
    json.dump(tareas, archivo, indent=2)

def ver_aciones():
  print("\n\n====================")
  print("======= MENÚ =======")
  print("====================")
  print("1. Agregar tarea")
  print("2. Ver tareas")
  print("3. Completar tarea")
  print("4. Eliminar tarea")
  print("5. Buscar tarea")
  print("6. Salir")


def agregar_tarea():
  print("Agregando")
  nuevo_titulo = input("Ingresa un titulo: ")
  nuevo_prioridad = input("Ingresa una prioridad: ")
  nuevo_completada = input("Esta completa? ")

  tareas.append({
    "titulo": nuevo_titulo,
    "completada": nuevo_completada,
    "prioridad": nuevo_prioridad
  })

  guardar_tareas_json()


def ver_tareas():
  if len(tareas) == 0:
    print("\nNo hay tareas")
  else:
    for tarea in tareas:
      print(f'Titulo: {tarea["titulo"]}')
      print(f'Prioridad: {tarea["prioridad"]} [Completada: {tarea["completada"]}]')


while True:
  ver_aciones()
  accion_seleccionada = validar_numero("\nIngresa la accion que deseas: ")
  
  if accion_seleccionada == 1:
    agregar_tarea()
  
  if accion_seleccionada == 2:
    ver_tareas()

  if accion_seleccionada == 6:
    break
    