import math
import json

try:
  with open("./00_exercices/json/historico_operaciones.json", "r") as operacion:
    historico = json.load(operacion)
except FileNotFoundError:
  historico = []

def guardar_historico():
  with open("./00_exercices/json/historico_operaciones.json", "w") as operacion:
    json.dump(historico, operacion, indent=2)

def imprimir_historico():
  #if len(historico) > 0:
  for h in historico:
    print(f"{h['operacion']}")

operaciones = {
  1: "+",
  2: "-",
  3: "*",
  4: "/",
  5: "^",
  6: "√",
  7: "h",
  8: "s"
}

def validar_numero(input_ingresado, entero = False):
  while True:
    try:
      numero = int(input(input_ingresado)) if entero else float(input(input_ingresado))
      return numero
    except ValueError:
      print("\nSolo se admiten números")

def ver_acciones():
  print("\n\n===== CALCULADORA =====")
  print("1. Sumar")
  print("2. Restar")
  print("3. Multiplicar")
  print("4. Dividir")
  print("5. Potencia")
  print("6. Raiz cuadrada")
  print("7. Historico")
  print("8. Salir")

def pedir_numeros(op):
  if op == "√":
    numero_1 = validar_numero("Número: ")
    return numero_1
  else:
    numero_1 = validar_numero("Primer número: ")
    numero_2 = validar_numero("Segundo número: ")

    return numero_1, numero_2
  
def operacion(op):
  if op == "√":
    n1 = pedir_numeros(op)
  else:
    n1, n2 = pedir_numeros(op)

  if op == "+":
    resultado = n1 + n2
  elif op == "-":
    resultado = n1 - n2
  elif op == "*":
    resultado = n1 * n2
  elif op == "/":
    if n2 == 0:
      print(f"El divisor debe ser diferente a 0")
      return
    resultado = n1 / n2
  elif op == "^":
    resultado = n1 ** n2
  elif op == "√":
    if n1 >= 0:
      resultado = math.sqrt(n1)
    else:
      print(f"La raiz cuadrada debe ser de un número positivo")
      return

  if op == "√":
    print(f"{op} {n1} = {resultado}")
    operacion_diccionario = f"{op} {n1} = {resultado}"

  else:
    print(f"{n1} {op} {n2} = {resultado}")
    operacion_diccionario = f"{n1} {op} {n2} = {resultado}"


  historico.append({
    "operacion": operacion_diccionario
  })

  guardar_historico()



while True:
  ver_acciones()

  operacion_seleccionada = validar_numero("Selecciona una operacion: ", True)

  if operacion_seleccionada not in operaciones:
    print("Número fuera de rango")
    continue

  if operacion_seleccionada == 8:
    break
  elif operacion_seleccionada == 7:
    imprimir_historico()
  else:
    operacion(operaciones[operacion_seleccionada])
