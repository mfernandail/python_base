# Métodos Útiles de Listas y Strings en Python

## Métodos Avanzados de Listas

| Método                  | Descripción                                   | Ejemplo                                           |
| ----------------------- | --------------------------------------------- | ------------------------------------------------- |
| `join()`                | Convierte lista de strings en un único string | `", ".join(["a", "b", "c"])` → `"a, b, c"`        |
| `split()`               | Convierte string en lista                     | `"a,b,c".split(",")` → `["a", "b", "c"]`          |
| `min()`                 | Retorna el elemento mínimo                    | `min([3, 1, 5])` → `1`                            |
| `max()`                 | Retorna el elemento máximo                    | `max([3, 1, 5])` → `5`                            |
| `sum()`                 | Suma todos los elementos                      | `sum([1, 2, 3])` → `6`                            |
| `len()`                 | Retorna la cantidad de elementos              | `len([1, 2, 3])` → `3`                            |
| `list(dict.fromkeys())` | Elimina duplicados manteniendo orden          | `list(dict.fromkeys([1, 2, 1, 3]))` → `[1, 2, 3]` |

## Métodos de Strings Útiles

| Método              | Descripción                        | Ejemplo                               |
| ------------------- | ---------------------------------- | ------------------------------------- |
| `upper()`           | Convierte a MAYÚSCULAS             | `"hola".upper()` → `"HOLA"`           |
| `lower()`           | Convierte a minúsculas             | `"HOLA".lower()` → `"hola"`           |
| `strip()`           | Elimina espacios al inicio y final | `"  hola  ".strip()` → `"hola"`       |
| `replace(old, new)` | Reemplaza texto                    | `"hola".replace("o", "0")` → `"h0la"` |
| `find(substring)`   | Busca posición de un string        | `"hola".find("o")` → `1`              |
| `startswith()`      | Verifica si empieza con            | `"hola".startswith("ho")` → `True`    |
| `endswith()`        | Verifica si termina con            | `"hola".endswith("la")` → `True`      |
| `isdigit()`         | Verifica si son solo dígitos       | `"123".isdigit()` → `True`            |
| `isalpha()`         | Verifica si son solo letras        | `"abc".isalpha()` → `True`            |

## Funciones Integradas Útiles

| Función        | Descripción                            | Ejemplo                                        |
| -------------- | -------------------------------------- | ---------------------------------------------- |
| `enumerate()`  | Itera con índice (para bucles)         | `for i, v in enumerate(lista):`                |
| `zip()`        | Combina múltiples listas (para bucles) | `zip([1,2], ["a","b"])` → `[(1,"a"), (2,"b")]` |
| `range()`      | Crea secuencia de números              | `range(0, 5)` → `0, 1, 2, 3, 4`                |
| `type()`       | Retorna el tipo de dato                | `type(5)` → `<class 'int'>`                    |
| `isinstance()` | Verifica si es de un tipo              | `isinstance(5, int)` → `True`                  |

## Ejemplos Prácticos

```python
# Trabajar con strings
email = "usuario@gmail.com"
nombre = email.split("@")[0]
print(nombre)  # usuario

# Buscar en lista
numeros = [3, 1, 4, 1, 5]
print(max(numeros))  # 5
print(numeros.count(1))  # 2

# Limpiar entrada
entrada = "  python  "
entrada_limpia = entrada.strip().upper()
print(entrada_limpia)  # PYTHON

# Eliminar duplicados manteniendo orden
valores = [12, 7, 5, 19, 12, 33, 7, 40, 5]
sin_duplicados = list(dict.fromkeys(valores))
print(sin_duplicados)  # [12, 7, 5, 19, 33, 40]
```

Estos métodos son muy útiles en desarrollo real para manipular datos, validar entradas, y procesar información.
