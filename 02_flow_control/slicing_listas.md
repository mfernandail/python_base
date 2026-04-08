# Slicing de Listas en Python

La sintaxis general es:

`lista[inicio:fin:paso]`

- `inicio` es inclusivo.
- `fin` es exclusivo.
- `paso` puede ser positivo o negativo.

| Slicing                  | Descripción breve                                             | Ejemplo                                           |
| ------------------------ | ------------------------------------------------------------- | ------------------------------------------------- |
| `lista[:]`               | Copia completa de la lista (shallow copy).                    | `nums = [0,1,2,3,4]` → `nums[:]` da `[0,1,2,3,4]` |
| `lista[inicio:fin]`      | Extrae desde `inicio` hasta `fin-1`.                          | `nums[1:4]` da `[1,2,3]`                          |
| `lista[:fin]`            | Desde el principio hasta `fin-1`.                             | `nums[:3]` da `[0,1,2]`                           |
| `lista[inicio:]`         | Desde `inicio` hasta el final.                                | `nums[2:]` da `[2,3,4]`                           |
| `lista[::paso]`          | Toda la lista avanzando de `paso` en `paso`.                  | `nums[::2]` da `[0,2,4]`                          |
| `lista[inicio:fin:paso]` | Sublista entre `inicio` y `fin` usando salto `paso`.          | `nums[1:5:2]` da `[1,3]`                          |
| `lista[::-1]`            | Invierte la lista.                                            | `nums[::-1]` da `[4,3,2,1,0]`                     |
| `lista[inicio:fin:-1]`   | Recorre hacia atrás en el rango indicado.                     | `nums[3:0:-1]` da `[3,2,1]`                       |
| `lista[-n:]`             | Últimos `n` elementos.                                        | `nums[-2:]` da `[3,4]`                            |
| `lista[:-n]`             | Todos excepto los últimos `n` elementos.                      | `nums[:-2]` da `[0,1,2]`                          |
| `lista[-n:-m]`           | Segmento usando índices negativos.                            | `nums[-4:-1]` da `[1,2,3]`                        |
| `lista[1:-1]`            | Todos excepto el primero y el último.                         | `nums[1:-1]` da `[1,2,3]`                         |
| `lista[:: -2]`           | Lista invertida tomando cada 2 elementos.                     | `nums[::-2]` da `[4,2,0]`                         |
| `lista[::1]`             | Recorre toda la lista sin saltos (equivale a copia).          | `nums[::1]` da `[0,1,2,3,4]`                      |
| `lista[5:5]`             | Slice vacío cuando inicio == fin.                             | `nums[2:2]` da `[]`                               |
| `lista[10:]`             | Fuera de rango: no falla, devuelve vacío si no hay elementos. | `nums[10:]` da `[]`                               |

## Notas rápidas

- El slicing nunca lanza `IndexError` por límites fuera de rango.
- El resultado de un slicing siempre es una nueva lista.
- Si `paso` es negativo, normalmente `inicio` debe ser mayor que `fin` para obtener elementos.
