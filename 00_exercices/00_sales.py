compras = []

def pedir_numero(mensaje, num_min = 0):
  while True:
    try:
      numero = int(input(mensaje))
      if numero >= num_min:
        return numero
      else:
        print(f"\nEl número debe ser mayor o igual a {num_min}")
    except:
      print("\nSolo se admiten números")
      

def agregar_compra():
  nombre_compra = input("Ingresa el nombre de un producto: ").lower()
  existe_compra = False

  if len(compras) > 0:
    for compra in compras:
      if compra["nombre"] == nombre_compra:
        existe_compra = True

  if existe_compra == False:
    cantidad_compra = pedir_numero("Ingresa la cantidad que quieres comprar: ", 1)
    precio_compra = pedir_numero("Ingrese el precio: ")
    
    compras.append({ "nombre": nombre_compra, "cantidad": cantidad_compra, "precio": precio_compra })
    print("\nProducto agregado correctamente")
    print(compras)

  else:
    print("\n==============================================================")
    print(f"El producto {nombre_compra} ya asta ingresado, edita su cantidad")
    print("==============================================================")


def ver_compras():
  if len(compras) == 0:
    print("\n==============================")
    print("Aun no hay compras realizadas")
    print("==============================")

  else:
    total_compra = 0
    for i, compra in enumerate(compras):
      total_compra += compra["cantidad"] * compra["precio"]
      print(f'{ i + 1 }. {compra["nombre"]} - Cantidad: {compra["cantidad"]}, ${compra["precio"]} por unidad - Total: {compra["cantidad"] * compra["precio"]}')
    
    print("\n=================================")
    print(f"El total de la compra es: ${total_compra}")
    print("=================================")

def eliminar_producto():
  for i, compra in enumerate(compras):
    print(f'Id: [{i}] {compra["nombre"]} - Cantidad: {compra["cantidad"]}, ${compra["precio"]} por unidad - Total: {compra["cantidad"] * compra["precio"]}')

  id_eliminar = pedir_numero("Ingresa el id a eliminar: ")
  
  if id_eliminar >= 0 and id_eliminar < len(compras):
    compras.pop(id_eliminar)
    for i, compra in enumerate(compras):
      print(f'{ i + 1 }. {compra["nombre"]} - Cantidad: {compra["cantidad"]}, ${compra["precio"]} por unidad - Total: {compra["cantidad"] * compra["precio"]}')
  else:
    print(f"\nId no encontrado {id_eliminar}")

def editar_compra():
  nombre_producto_busqueda = input("Ingresa el nombre del producto: ").lower()
  producto_encontrado = False
  
  for compra in compras:
    if compra["nombre"] == nombre_producto_busqueda:
      producto_encontrado = True
      print(f"\nCompra: {compra['nombre']} ({compra['cantidad']})")
      
        
      
      while True:
        cantidad_editar = pedir_numero("Ingresa la cantidad: ")
        if cantidad_editar > 0:
          compra["cantidad"] = cantidad_editar
          print(f"Listo! se ha editado a {cantidad_editar}")
          break
        else:
          print("\nLa cantidad debe ser mayor a cero 0")
      
          
      
  if not producto_encontrado:
    print("=========================")
    print("= Producto no ecnotrado =")
    print("=========================")

def mostrar_menu():
  print("\n\n====================")
  print("======= MENÚ =======")
  print("====================")
  print("\n1. Agregar producto")
  print("2. Ver lista")
  print("3. Eliminar producto")
  print("4. Editar producto")
  print("5. Salir")

while True:
  mostrar_menu()
  
  respuesta = pedir_numero("\n¿Cual opcion eliges? ")

  if respuesta == 1:
    agregar_compra()
  
  elif respuesta == 2:
    ver_compras()
  
  elif respuesta == 3:
    eliminar_producto()
  
  elif respuesta == 4:
    editar_compra()
    
  elif respuesta == 5:
    print("\nSaliendo, gracias por venir.")
    break
  
  else:
    print("Opción inválida")