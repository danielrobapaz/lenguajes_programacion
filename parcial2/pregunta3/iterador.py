"""
    Implementacion de un iterador que dada un lista de enteros con elementos unicos,
    devuelve todas las sublistas crecientes que contiene.

    Daniel Robayo, 18-11086
"""

def esta_ordenada(lista: [int]):
    return all(lista[i] < lista[i+1] for i in range(len(lista)-1))

def iterador(lista: [int]):
    if len(lista) != len(set(lista)):
        raise Exception("La lista no puede contener elementos repetidos")
    
    if lista == []:
        yield []
    else:
        for x in iterador(lista[1:]):
            yield x
            if esta_ordenada([lista[0], *x]):
                yield [lista[0], *x]