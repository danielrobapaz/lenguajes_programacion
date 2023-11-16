"""
    Implementacion de las subrutinas para calcular el valor 
    de la familia de funciones dada

    Hay tres versiones.
        - recursiva
        - de cola
        - iterativa

    Daniel Robayo, 18-11086
"""
def actualizar_acumulador(acum: [int]):
        new_acum = [acum[i] for i in range(1, len(acum))]
        last_acum = acum[35] + acum[28] + acum[21] + acum[14] + acum[7] + acum[0]

        return  new_acum + [last_acum]

def recursiva(n: int) -> int:
    """
        Implementacion recurisva directa de la formula de la familia de funciones
    """
    if n < 42:
        return n

    return recursiva(n-7) + recursiva(n-14) + recursiva(n-21) + recursiva(n-28) + recursiva(n-35) + recursiva(n-42)

def cola(n: int) -> int:
    """
        Implementacion de recusion de cola de la version recursiva de la formula
        de la familia de funciones.
    """
    def recursion_cola(n: int,
                       i: int = 41,
                       acum: [int] = [i for i in range(42)]) -> int:
        # todos los casos base
        if n < 42:
            return acum[n]
        
        if n==i:
            return acum[41]

        return recursion_cola(n, i+1, actualizar_acumulador(acum))
    
    return recursion_cola(n)

def iterativa(n: int) -> int:
    if n < 42:
        return n
    
    i = 41 # corresponde a la condicion de parada
    acum = [j for j in range(42)]

    while (i < n):
        acum = actualizar_acumulador(acum)        
        i += 1
    return acum[41]