import os
os.system("clear")

lista_frutas = ["Manzana", "Platano", "Naranja", "Frutilla", "Uva"]

print("\nLista de frutas:")
print(lista_frutas)  # Imprime toda la lista de frutas
print(lista_frutas[0])  # Imprime "Manzana"
print(lista_frutas[-1])  # Imprime "Uva"
print(lista_frutas[1:4])  # Imprime ["Platano", "Naranja", "Frutilla"]


lista_matrices = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nLista de matrices:")
print(lista_matrices)  # Imprime toda la lista de matrices
print(lista_matrices[0])  # Imprime [1, 2, 3]
print(lista_matrices[1][2])  # Imprime 6


lista_numeros = [10, 20, 30, 40, 50]
print("\nLista de números:")
print(lista_numeros[:3])  # Imprime los primeros 3 elementos: [10, 20, 30]
print(lista_numeros[2:])  # Imprime desde el índice 2 hasta el final: [30, 40, 50]
print(lista_numeros[::2])  # Imprime cada segundo elemento: [10, 30, 50]
print(lista_numeros[:]) # Imprime toda la lista: [10, 20, 30, 40, 50]
print(lista_numeros[::-1]) # Imprime la lista al revés: [50, 40, 30, 20, 10]

# Agregar elementos a la lista
lista_numeros = lista_numeros + [60, 70, 80]

lista_numeros += [60, 70, 80]

# Otra forma de agregar elementos a la lista es utilizando el método append()
lista_numeros.append(90)

# Longitud de la lista
print("\nLongitud de la lista de números:")
print(len(lista_numeros))  # Imprime la longitud de la lista de números