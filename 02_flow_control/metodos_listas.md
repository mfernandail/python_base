# Métodos de las Listas en Python

| Método             | Descripción                                                                   | Ejemplo                                                        |
| ------------------ | ----------------------------------------------------------------------------- | -------------------------------------------------------------- |
| `append(x)`        | Agrega un elemento al final de la lista                                       | `lista.append("Mango")` → `["Manzana", "Mango"]`               |
| `insert(i, x)`     | Inserta un elemento en la posición indicada                                   | `lista.insert(1, "Mango")` → `["Manzana", "Mango", "Platano"]` |
| `extend(iterable)` | Agrega todos los elementos de otro iterable al final                          | `lista.extend(["Mango", "Kiwi"])`                              |
| `remove(x)`        | Elimina la primera aparición del elemento indicado                            | `lista.remove("Platano")`                                      |
| `pop(i)`           | Elimina y retorna el elemento en la posición indicada (por defecto el último) | `lista.pop()` → `"Uva"`                                        |
| `clear()`          | Elimina todos los elementos de la lista                                       | `lista.clear()` → `[]`                                         |
| `index(x)`         | Retorna el índice de la primera aparición del elemento                        | `lista.index("Naranja")` → `2`                                 |
| `count(x)`         | Retorna cuántas veces aparece el elemento en la lista                         | `lista.count("Manzana")` → `1`                                 |
| `sort()`           | Ordena los elementos de la lista en orden ascendente (modifica la lista)      | `lista.sort()` → `["Frutilla", "Manzana", "Naranja"]`          |
| `reverse()`        | Invierte el orden de los elementos de la lista                                | `lista.reverse()` → `["Uva", "Frutilla", "Naranja"]`           |
| `copy()`           | Retorna una copia superficial de la lista                                     | `nueva = lista.copy()`                                         |
