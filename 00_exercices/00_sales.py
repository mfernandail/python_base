# Crea una lista vacía llamada "compras"

compras = []

# Inicia un ciclo infinito (while True)
while True:
  print("\n")
  print("1. Agregar producto")
  print("2. Ver lista")
  print("3. Salir")
  print("4. Eliminar producto")
  
  respuesta = int(input("\n¿Cual opcion eliges? "))

  if respuesta == 1:
    nombre_producto = input("Ingresa el nombre de un producto: ")
    compras.append(nombre_producto)
    
  elif respuesta == 2:
    if len(compras) == 0:
      print("Lista vacía")
    else:
      for i, compra in enumerate(compras):
        print(f"Compras #{i + 1}: {compra}")
    
  elif respuesta == 3:
    print("Saliendo")
    break
  
  elif respuesta == 4:
    print(f"¿Qué número eliminar?")
    for i, compra in enumerate(compras):
      print(f"Id: {i} ({compra})")
    
    id_eliminar = int(input("Ingrese el id: "))
    
    if id_eliminar > 0 & id_eliminar < len(compras):
      compras.pop(id_eliminar)
    else:
      print(f"El id: {id_eliminar} no existe")
    
  else:
    print("opción no es válida")  

    # Pide al usuario una opción

    # Si la opción es 1:
        # Pide el nombre de un producto
        # Agrega el producto a la lista

    # Si la opción es 2:
        # Verifica si la lista está vacía
            # Si está vacía, muestra "Lista vacía"
            # Si no:
                # Recorre la lista
                # Muestra cada producto

    # Si la opción es 3:
        # Termina el programa (break)

    # Si la opción no es válida:1
        # Muestra mensaje de error