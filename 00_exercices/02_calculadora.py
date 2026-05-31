def validar_numero(input_ingresado, num_min = 0):
  while True:
    try:
      numero = int(input(input_ingresado))
      if numero >= num_min:
        return numero
      else:
        print(f"\nEl número debe ser mayor o igual a {num_min}")
    except ValueError:
      print("\nSolo se admiten números")

def ver_acciones():
  print("\n\n===== CALCULADORA =====")
  print("1. Sumar")
  print("2. Restar")
  print("3. Multiplicar")
  print("4. Dividir")
  print("5. Salir")


while True:
  ver_acciones()

  operacion_seleccionada = validar_numero("Selecciona una operacion: ", 1)

  print(f"Seleccionaste: {operacion_seleccionada}")
