# Solucion parcial 1
Para evitar inconsistencia, los programas entregados se deben ejecutar en un sistema operativo _linux-like_

## Pregunta 1

### (a)

### (b)
- solucion en rotar.d
    ```
    $dmd rotar.d
    $./rotar [string] chars_rotate
    ```
### (c)
- solucion en matri.d
    ```
    $dmd matrix.d
    $./matrix
    ```
- El programa recibe N, el tamano de la matriz, y la matriz fila a fila separando los numeros por espaciones. en input.input se encuentra un ejemplo. Se recomienda ejecutar el programa de la siguiente manera
    ```
    $./matrix < input.input
    ```