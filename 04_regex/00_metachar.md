# Regex en Python - Metacaracteres

## Resumen rápido

| Metachar | Significado            |
| -------- | ---------------------- |
| `\d`     | Dígito                 |
| `\D`     | No dígito              |
| `\w`     | Letra, número o `_`    |
| `\W`     | No letra, número o `_` |
| `\s`     | Espacio en blanco      |
| `\S`     | No espacio             |
| `.`      | Cualquier carácter     |
| `^`      | Inicio                 |
| `$`      | Final                  |
| `\A`     | Inicio absoluto        |
| `\Z`     | Final absoluto         |
| `\b`     | Límite de palabra      |
| `\B`     | No límite de palabra   |
| `*`      | 0 o más                |
| `+`      | 1 o más                |
| `?`      | 0 o 1                  |
| `{n}`    | Exactamente n          |
| `{n,}`   | n o más                |
| `{n,m}`  | Entre n y m            |
| `[]`     | Conjunto               |
| `[^]`    | Negación               |
| `-`      | Rango                  |
| `\| `    | OR                     |
| `()`     | Grupo                  |
| `(?:)`   | Grupo no capturante    |
| `\`      | Escapar caracteres     |

## Clases de caracteres predefinidas

### \d

Coincide con cualquier dígito.

```python
\d
```

Equivale a:

```python
[0-9]
```

Ejemplos:

```python
re.findall(r"\d", "abc123")
# ['1', '2', '3']
```

---

### \D

Coincide con cualquier carácter que NO sea un dígito.

```python
\D
```

Ejemplos:

```python
re.findall(r"\D", "abc123")
# ['a', 'b', 'c']
```

---

### \w

Coincide con:

- Letras
- Números
- Guion bajo `_`

```python
\w
```

Equivale aproximadamente a:

```python
[a-zA-Z0-9_]
```

Ejemplos:

```python
re.findall(r"\w", "hola_123!")
# ['h', 'o', 'l', 'a', '_', '1', '2', '3']
```

---

### \W

Coincide con cualquier carácter que NO sea:

- Letra
- Número
- Guion bajo

```python
\W
```

Ejemplos:

```python
re.findall(r"\W", "hola_123!")
# ['!']
```

---

### \s

Coincide con espacios en blanco.

Incluye:

- espacio
- tabulación
- salto de línea
- retorno de carro

```python
\s
```

Ejemplos:

```python
re.findall(r"\s", "hola mundo")
# [' ']
```

---

### \S

Coincide con cualquier carácter que NO sea espacio.

```python
\S
```

Ejemplos:

```python
re.findall(r"\S", "hola mundo")
# ['h', 'o', 'l', 'a', 'm', 'u', 'n', 'd', 'o']
```

---

## Anclas

### ^

Inicio de la cadena.

```python
^Hola
```

Coincide con:

```text
Hola mundo
```

No coincide con:

```text
Mi Hola mundo
```

---

### $

Final de la cadena.

```python
mundo$
```

Coincide con:

```text
Hola mundo
```

---

### \A

Inicio absoluto del texto.

```python
\AHola
```

Más estricto que `^`.

---

### \Z

Final absoluto del texto.

```python
mundo\Z
```

Más estricto que `$`.

---

### \b

Límite de palabra.

```python
\bcat\b
```

Coincide con:

```text
cat
```

No coincide con:

```text
catalog
```

---

### \B

No límite de palabra.

```python
\Bcat\B
```

Coincide solo si está dentro de otra palabra.

---

## Comodines

### .

Coincide con cualquier carácter excepto salto de línea.

```python
.
```

Ejemplos:

```python
a.c
```

Coincide con:

```text
abc
a1c
a-c
```

---

## Cuantificadores

### \*

Cero o más veces.

```python
ab*
```

Coincide con:

```text
a
ab
abb
abbb
```

---

### +

Una o más veces.

```python
ab+
```

Coincide con:

```text
ab
abb
abbb
```

No coincide con:

```text
a
```

---

### ?

Cero o una vez.

```python
colou?r
```

Coincide con:

```text
color
colour
```

---

### {n}

Exactamente n veces.

```python
\d{4}
```

Coincide con:

```text
2025
```

---

### {n,}

Al menos n veces.

```python
\d{2,}
```

Coincide con:

```text
12
123
12345
```

---

### {n,m}

Entre n y m veces.

```python
\d{2,4}
```

Coincide con:

```text
12
123
1234
```

---

## Conjuntos de caracteres

### []

Coincide con cualquiera de los caracteres indicados.

```python
[abc]
```

Coincide con:

```text
a
b
c
```

---

### [^]

Negación dentro de corchetes.

```python
[^abc]
```

Coincide con cualquier carácter excepto:

```text
a
b
c
```

---

### -

Rango dentro de corchetes.

```python
[a-z]
```

Letras minúsculas.

```python
[A-Z]
```

Mayúsculas.

```python
[0-9]
```

Dígitos.

---

## Alternativas

### |

Operador OR.

```python
gato|perro
```

Coincide con:

```text
gato
perro
```

---

## Agrupación

### (...)

Grupo capturante.

```python
(\d+)
```

Permite usar:

```python
group()
group(1)
groups()
```

---

### (?:...)

Grupo no capturante.

```python
(?:abc)
```

Agrupa sin guardar.

---

## Escapado

### \

Permite buscar caracteres especiales literalmente.

```python
\.
```

Busca:

```text
.
```

---

```python
\*
```

Busca:

```text
*
```

---

```python
\?
```

Busca:

```text
?
```

---
