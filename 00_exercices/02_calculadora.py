operaciones = {
  1: "+",
  2: "-",
  3: "*",
  4: "/"
}

def validar_numero(input_ingresado):
  while True:
    try:
      numero = int(input(input_ingresado))
      return numero
    except ValueError:
      print("\nSolo se admiten números")

def ver_acciones():
  print("\n\n===== CALCULADORA =====")
  print("1. Sumar")
  print("2. Restar")
  print("3. Multiplicar")
  print("4. Dividir")
  print("5. Salir")

def pedir_numeros():
  numero_1 = validar_numero("Primer número: ")
  numero_2 = validar_numero("Segundo número: ")

  return numero_1, numero_2

def operacion(op):
  n1, n2 = pedir_numeros()

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
  
  print(f"{n1} {op} {n2} = {resultado}")

while True:
  ver_acciones()

  operacion_seleccionada = validar_numero("Selecciona una operacion: ")

  if operacion_seleccionada < 1 or operacion_seleccionada > 5:
    print("Número fuera de rango")
    continue
  if operacion_seleccionada == 5:
    break
  else:
    operacion(operaciones[operacion_seleccionada])
