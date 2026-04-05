import os
os.system("clear")

print("\nMethods")

list_of_numbers = [1, 2, 3, 4, 5, 3, 3, 3]
list_of_numbers.append(6)
print(list_of_numbers)

list_of_numbers.insert(0, 0)
print(list_of_numbers)

list_of_numbers.remove(3) # Se pasa el valor a eliminar, no el índice
print(list_of_numbers)

list_of_numbers.pop() # Elimina el último elemento de la lista
print(list_of_numbers)

list_of_numbers.pop(0) # Elimina el elemento en el índice 0
print(list_of_numbers)

list_of_numbers.pop(-1) # Elimina el último elemento de la lista
print(list_of_numbers)

del list_of_numbers[0] # Elimina el elemento en el índice 0
print(list_of_numbers)

list_of_numbers.clear() # Elimina todos los elementos de la lista
print(list_of_numbers)


# Ordenar listas modificando la lista original
list_of_numbers = [5, 2, 9, 1, 3]
list_of_numbers.sort()
print(list_of_numbers)

# Ordenar listas sin modificar la lista original
list_of_numbers = [5, 2, 9, 1, 3]
sorted_list = sorted(list_of_numbers)
print(list_of_numbers)
print(sorted_list)

# La diferencia entre sort() y sorted() es que sort() modifica la lista original, mientras que sorted() devuelve una nueva lista ordenada sin modificar la original.

animals = ["dog", "cat", "elephant", "bear", "ant", "cat", "cat"]
print(animals)
print(animals.count("cat")) # Cuenta cuántas veces aparece "cat" en la lista
print('cat' in animals) # Verifica si "cat" está en la lista
print(animals.index("cat")) # Devuelve el índice de la primera aparición de "cat