# Roadmap de Aprendizaje Python

## Objetivo

Dominar Python desde nivel principiante hasta nivel intermedio mediante proyectos prácticos, comprendiendo los fundamentos del lenguaje, la programación orientada a objetos, el manejo de archivos y bases de datos.

---

# Nivel 1: Fundamentos de Python

## Variables y tipos de datos

Aprender:

- int
- float
- str
- bool
- None

Ejemplos:

```python
edad = 30
precio = 19.99
nombre = "María"
activo = True
```

### Conceptos

- Asignación de variables
- Conversión de tipos (`int()`, `str()`, `float()`)
- Operadores matemáticos
- Operadores de comparación
- Operadores lógicos

---

## Entrada y salida de datos

Aprender:

```python
input()
print()
```

### Conceptos

- Capturar datos del usuario
- Formatear texto
- f-strings

```python
print(f"Hola {nombre}")
```

---

## Condicionales

Aprender:

```python
if
elif
else
```

### Conceptos

- Toma de decisiones
- Comparaciones
- Operadores lógicos

---

## Bucles

### While

```python
while condicion:
    pass
```

### For

```python
for item in lista:
    pass
```

### Conceptos

- Iteración
- break
- continue
- range()

---

# Nivel 2: Estructuras de Datos

## Listas

Aprender:

```python
gastos = []
```

Métodos:

- append()
- remove()
- pop()
- sort()
- reverse()

### Conceptos

- Índices
- Recorrido
- Modificación de elementos

---

## Diccionarios

Aprender:

```python
gasto = {
    "descripcion": "Pan",
    "monto": 1000
}
```

Métodos:

- keys()
- values()
- items()
- get()

### Conceptos

- Clave-valor
- Acceso seguro a datos

---

## Tuplas

Aprender:

```python
coordenada = (10, 20)
```

### Conceptos

- Inmutabilidad

---

## Sets

Aprender:

```python
categorias = set()
```

### Conceptos

- Valores únicos
- Eliminar duplicados

---

# Nivel 3: Funciones

## Crear funciones

Aprender:

```python
def saludar():
    pass
```

## Parámetros

```python
def saludar(nombre):
    pass
```

## Return

```python
def sumar(a, b):
    return a + b
```

### Conceptos

- Parámetros
- Argumentos
- Valores por defecto
- Retorno
- Scope (variables locales y globales)

---

# Nivel 4: Manejo de Errores

## Try / Except

Aprender:

```python
try:
    pass
except ValueError:
    pass
```

Errores comunes:

- ValueError
- FileNotFoundError
- KeyError
- ZeroDivisionError

### Conceptos

- Programación defensiva
- Validación de datos

---

# Nivel 5: Comprensiones

## List Comprehension

Aprender:

```python
cuadrados = [x**2 for x in range(10)]
```

## Filtrado

```python
comidas = [
    gasto
    for gasto in gastos
    if gasto["categoria"] == "Comida"
]
```

### Conceptos

- Crear listas de forma eficiente
- Filtrar información

---

# Nivel 6: Archivos

## Lectura y escritura

Aprender:

```python
with open("archivo.txt") as archivo:
    pass
```

### Formatos

- TXT
- JSON
- CSV

---

## JSON

Aprender:

```python
import json
```

Funciones:

- json.load()
- json.dump()

### Conceptos

- Persistencia de datos
- Serialización

---

## Pathlib

Aprender:

```python
from pathlib import Path
```

### Conceptos

- Rutas multiplataforma
- Manejo seguro de archivos

---

# Nivel 7: Programación Orientada a Objetos (POO)

## Clases

Aprender:

```python
class Gasto:
    pass
```

## Constructores

```python
def __init__(self):
    pass
```

## Objetos

```python
gasto = Gasto()
```

### Conceptos

- Clase
- Objeto
- Atributo
- Método
- Encapsulación

---

# Nivel 8: Modularización

## Separar código

Estructura:

```text
proyecto/
│
├── main.py
├── gastos.py
├── validaciones.py
├── json_manager.py
```

### Conceptos

- Importaciones
- Reutilización
- Organización del código

---

# Nivel 9: Algoritmos y Estructuras de Datos

## Búsqueda

Aprender:

- Búsqueda lineal

```python
for item in lista:
    pass
```

---

## Ordenamiento

Aprender:

```python
sorted()
```

```python
lista.sort()
```

---

## Complejidad básica

Conceptos:

- O(1)
- O(n)
- O(n²)

Objetivo:

Comprender por qué algunas soluciones son más eficientes que otras.

---

# Nivel 10: Testing

## Assert

Aprender:

```python
assert total == 1000
```

## Unit Testing

Aprender:

```python
import unittest
```

o

```python
pytest
```

### Conceptos

- Pruebas automáticas
- Verificación de funciones

---

# Nivel 11: Bases de Datos

## SQLite

Aprender:

```python
import sqlite3
```

Consultas básicas:

```sql
CREATE TABLE
INSERT INTO
SELECT
UPDATE
DELETE
```

### Conceptos

- Persistencia de datos
- CRUD
- Relaciones básicas

---

# Nivel 12: Git y GitHub

## Git

Comandos básicos:

```bash
git init
git add .
git commit -m "mensaje"
git status
git log
```

## GitHub

Aprender:

- Crear repositorios
- Subir proyectos
- Clonar proyectos

---

# Nivel 13: Entornos Virtuales

Aprender:

```bash
python -m venv venv
```

Activar:

```bash
source venv/bin/activate
```

o

```bash
venv\Scripts\activate
```

### Conceptos

- Dependencias
- Aislamiento de proyectos

---

# Nivel 14: Librerías Externas

## Pip

Aprender:

```bash
pip install requests
```

### Librerías recomendadas

- requests
- pandas
- matplotlib

---

# Nivel 15: Interfaces Gráficas

## Tkinter

Aprender:

```python
import tkinter
```

### Conceptos

- Ventanas
- Botones
- Inputs
- Eventos

---

# Proyectos Recomendados

## Principiante

- Gestor de gastos
- Agenda de contactos
- Lista de tareas
- Inventario simple
- Biblioteca de libros

## Intermedio

- Sistema de ventas
- Control de stock
- Gestor de notas
- Sistema de reservas
- Conversor de monedas

## Intermedio Avanzado

- Gestor de gastos con SQLite
- Aplicación con Tkinter
- Dashboard financiero
- Consumo de APIs
- Web Scraping básico

---

# Estado Actual

Ya domino:

- Variables
- Condicionales
- Bucles
- Funciones
- Listas
- Diccionarios
- Manejo de errores básico
- JSON
- Validación de datos
- Menús interactivos
- Persistencia en archivos

Próximos objetivos:

1. Completar CRUD del gestor de gastos.
2. Aprender comprensión de listas.
3. Aprender Programación Orientada a Objetos.
4. Aprender SQLite.
5. Aprender Git y GitHub.
