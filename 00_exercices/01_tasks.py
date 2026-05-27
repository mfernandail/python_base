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
    except ValueError:
      print("\nSolo se admiten números")

def guardar_tareas_json():
  with open("./00_exercices/json/tareas.json", "w") as archivo:
    json.dump(tareas, archivo, indent=2)

def ver_acciones():
  print("\n\n====================")
  print("======= MENÚ =======")
  print("====================")
  print("1. Agregar tarea")
  print("2. Ver tareas")
  print("3. Completar tarea")
  print("4. Eliminar tarea")
  print("5. Buscar tarea")
  print("6. Salir")

def validar_campos(pregunta, opcion = 1):
  while True:
    respuesta = input(pregunta).lower().strip()

    if len(respuesta) == 0:
      print("\n❗️ Ingresa una respuesta\n")
      continue

    if opcion == 2:
      if respuesta in ["alta", "media", "baja"]:
        return respuesta
      else:
        print("\n❗ La prioridad debe ser: alta, media o baja\n")
    elif opcion == 3:
      if respuesta in ["true", "false"]:
        return respuesta == "true"
      else:
        print("\n❗ Solo puedes escribir: true o false\n")
    else:
      return respuesta

    

def agregar_tarea():
  nueva_titulo = validar_campos("Ingresa un titulo: ")
  nueva_prioridad = validar_campos("Ingresa una prioridad: ", 2)
  nueva_completada = validar_campos("Esta completa? ", 3)

  tareas.append({
    "titulo": nueva_titulo,
    "completada": nueva_completada,
    "prioridad": nueva_prioridad
  })

  guardar_tareas_json()



def ver_tareas():
  if len(tareas) == 0:
    print("\nNo hay tareas")
  else:
    print("\n-------------------------------------------------")
    for tarea in tareas:
      if tarea["completada"]:
        estado_tarea = "✅"
      else:
        estado_tarea = "❌"
      
      if tarea["prioridad"] == "alta":
        prioridad_tarea = "🔴"
      elif tarea["prioridad"] == "media":
        prioridad_tarea = "🟡"
      else:
        prioridad_tarea = "🟢"

      print(f'{estado_tarea} | {prioridad_tarea} | Titulo: {tarea["titulo"]} ')
      print("-------------------------------------------------")

def completar_tarea():
  for i, tarea in enumerate(tareas):
    print("\nListado de tareas: ")
    print(f'[{i}] Tarea: {tarea["titulo"]}')

  id_tarea_completar = validar_numero("\n¿Que tarea quieres completar? ", 0)

  print(type(id_tarea_completar))

  for i, tarea in enumerate(tareas):
    if i == id_tarea_completar:
      tarea["completada"] = True
      break
  

def eliminar_tarea():
  print("Eliminando")
  for i, tarea in enumerate(tareas):
    print("\nListado de tareas: ")
    print(f'[{i}] Tarea: {tarea["titulo"]}')

  id_tarea_eliminar = validar_numero("\n¿Que tarea quieres eliminar? ", 0)

  tareas.pop(id_tarea_eliminar)

def buscar_tarea():
  print("Buscar tarea")

while True:
  ver_acciones()

  accion_seleccionada = validar_numero("\nIngresa la accion que deseas: ")
  
  if accion_seleccionada == 1:
    agregar_tarea()
  
  elif accion_seleccionada == 2:
    ver_tareas()
  
  elif accion_seleccionada == 3:
    completar_tarea()

  elif accion_seleccionada == 4:
    eliminar_tarea()

  elif accion_seleccionada == 5:
    buscar_tarea()

  elif accion_seleccionada == 6:
    break
    