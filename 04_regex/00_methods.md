# Regex en Python - Métodos y Funciones

```python
import re
```

## Objeto Match

Un objeto `Match` es el resultado de una búsqueda exitosa.

```python
resultado = re.search(r"\d+", "Tengo 123 años")
```

---

## group()

Devuelve la coincidencia encontrada.

```python
resultado.group()
# '123'
```

También puede devolver grupos específicos:

```python
resultado = re.search(r"(\w+) (\w+)", "Juan Pérez")

resultado.group(1)
# 'Juan'

resultado.group(2)
# 'Pérez'
```

---

## groups()

Devuelve todos los grupos capturados como una tupla.

```python
resultado.groups()
# ('Juan', 'Pérez')
```

---

## groupdict()

Devuelve grupos nombrados como diccionario.

```python
resultado = re.search(
    r"(?P<nombre>\w+) (?P<apellido>\w+)",
    "Juan Pérez"
)

resultado.groupdict()

# {'nombre': 'Juan', 'apellido': 'Pérez'}
```

---

## start()

Posición inicial de la coincidencia.

```python
resultado.start()
# 6
```

---

## end()

Posición final de la coincidencia.

```python
resultado.end()
# 9
```

---

## span()

Devuelve `(inicio, fin)`.

```python
resultado.span()
# (6, 9)
```

---

## string

Texto completo analizado.

```python
resultado.string
# 'Tengo 123 años'
```

---

## re

Patrón utilizado.

```python
resultado.re
# re.compile('\\d+')
```

---

## lastindex

Último grupo capturado.

```python
resultado.lastindex
```

---

## lastgroup

Nombre del último grupo capturado.

```python
resultado.lastgroup
```

---

# Funciones del módulo re

## re.match()

Busca sólo al inicio del texto.

```python
re.match(r"\d+", "123abc")
```

✅ Coincide

```python
re.match(r"\d+", "abc123")
```

❌ No coincide

---

## re.search()

Busca la primera coincidencia en cualquier parte.

```python
re.search(r"\d+", "abc123")
```

✅ Encuentra "123"

---

## re.findall()

Devuelve todas las coincidencias.

```python
re.findall(r"\d+", "123 abc 456")
```

Resultado:

```python
['123', '456']
```

---

## re.finditer()

Devuelve un iterador de objetos Match.

```python
for m in re.finditer(r"\d+", "123 abc 456"):
    print(m.group())
```

Salida:

```python
123
456
```

---

## re.fullmatch()

Toda la cadena debe coincidir.

```python
re.fullmatch(r"\d+", "123")
```

✅

```python
re.fullmatch(r"\d+", "123abc")
```

❌

---

## re.sub()

Reemplaza coincidencias.

```python
re.sub(r"\d+", "X", "123 abc 456")
```

Resultado:

```python
'X abc X'
```

---

## re.subn()

Igual que `sub()`, pero devuelve cantidad de reemplazos.

```python
re.subn(r"\d+", "X", "123 abc 456")
```

Resultado:

```python
('X abc X', 2)
```

---

## re.split()

Divide usando un patrón.

```python
re.split(r",\s*", "manzana, pera, kiwi")
```

Resultado:

```python
['manzana', 'pera', 'kiwi']
```

---

## re.compile()

Compila un patrón para reutilizarlo.

```python
patron = re.compile(r"\d+")

patron.search("abc123")
```

---

# Flags (modificadores)

## re.IGNORECASE

Ignora mayúsculas/minúsculas.

```python
re.search(r"python", "PYTHON", re.IGNORECASE)
```

---

## re.MULTILINE

`^` y `$` funcionan por línea.

```python
re.search(r"^Hola", texto, re.MULTILINE)
```

---

## re.DOTALL

`.` coincide también con saltos de línea.

```python
re.search(r".+", texto, re.DOTALL)
```

---

## re.VERBOSE

Permite escribir regex comentadas.

```python
patron = re.compile(r"""
    \d+     # uno o más dígitos
    \s*     # espacios opcionales
    \w+     # palabra
""", re.VERBOSE)
```

---

# Métodos de Pattern (regex compilada)

```python
patron = re.compile(r"\d+")
```

## patron.search()

```python
patron.search("abc123")
```

---

## patron.match()

```python
patron.match("123abc")
```

---

## patron.fullmatch()

```python
patron.fullmatch("123")
```

---

## patron.findall()

```python
patron.findall("123 abc 456")
```

---

## patron.finditer()

```python
patron.finditer("123 abc 456")
```

---

## patron.sub()

```python
patron.sub("X", "123 abc 456")
```

---

## patron.split()

```python
patron.split("123 abc 456")
```

---

# Grupos especiales

## Grupo normal

```python
(\d+)
```

---

## Grupo nombrado

```python
(?P<edad>\d+)
```

---

## Grupo no capturante

```python
(?:abc)
```

---

## Lookahead positivo

```python
\d+(?=€)
```

Coincide con números seguidos de €.

---

## Lookahead negativo

```python
\d+(?!€)
```

---

## Lookbehind positivo

```python
(?<=\$)\d+
```

Coincide con números precedidos por $.

---

## Lookbehind negativo

```python
(?<!\$)\d+
```
