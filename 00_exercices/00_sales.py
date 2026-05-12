compras = []

def pedir_numero(mensaje):
  while True:
    try:
      numero = int(input(mensaje))
      return numero
    except:
      print("Solo se admiten números")
      

while True:
  print("\n")
  print("1. Agregar producto")
  print("2. Ver lista")
  print("3. Salir")
  print("4. Eliminar producto")
  print("5. Editar producto")
  
  respuesta = pedir_numero("\n¿Cual opcion eliges? ")
  
  if respuesta == 1:
    nombre_producto = input("Ingresa el nombre de un producto: ")
    cantidad_producto = pedir_numero("Ingresa la cantidad: ")
    
    compras.append({
      "nombre": nombre_producto,
      "cantidad": cantidad_producto
    })
    
  elif respuesta == 2:
    if len(compras) == 0:
      print("Lista vacía")
    else:
      print("\n")
      for i, compra in enumerate(compras):
        print(f"Compras #{i + 1}: {compra}")
    
  elif respuesta == 3:
    print("Saliendo")
    break
  
  elif respuesta == 4:
    print(f"¿Qué número eliminar?")
    for i, compra in enumerate(compras):
      print(f"Id: {i} ({compra})")
    
    id_eliminar = pedir_numero("Ingrese el id: ")
    
    if id_eliminar >= 0 and id_eliminar < len(compras):
      compras.pop(id_eliminar)
    else:
      print(f"El id: {id_eliminar} no existe")
  
  elif respuesta == 5:
    nombre_producto_buscar = input("¿Qué producto quieres editar? ")

    encontrado = False
    
    for compra in compras:
      if compra["nombre"] == nombre_producto_buscar:
        encontrado = True
    
        print(f"Producto encontrado: {nombre_producto_buscar} - cantidad: {compra["cantidad"]}")    
        nueva_cantidad = pedir_numero(f"Ingresa la nueva cantidad para {nombre_producto_buscar}: ")
        
        compra["cantidad"] = nueva_cantidad
        break

    if not encontrado:
      print(f"Producto: {nombre_producto_buscar} no encontrado")
  
  else:
    print("opción no es válida")  