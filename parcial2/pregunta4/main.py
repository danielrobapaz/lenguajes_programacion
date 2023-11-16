"""
    Creacion de un archivo csv que contiene
    el tamano del n y el tiempo de ejecucion de 
    cada algoritmo

    Daniel Robayo, 18-11086
"""
from Familia_De_Funciones import (recursiva, cola, iterativa)
import time
import pandas as pd

def calculate_time(func, n: int) -> float:
    start = time.time()
    n = func(n)
    return round(time.time() - start, 12)

def main(): 
    sizes_of_n = [n for n in range(0, 300, 10)]    
    df = pd.DataFrame(columns=['n', 'tiempo_recursivo', 'tiempo_recursivo_cola', 'tiempo_iterativo'])

    for n in sizes_of_n:
        print(n)
        curr_df = pd.DataFrame(data={
            'n': [n],
            'tiempo_recursivo': [calculate_time(recursiva, n)],
            'tiempo_recursivo_cola': [calculate_time(cola, n)],
            'tiempo_iterativo': [calculate_time(iterativa, n)]
        })

        df = pd.concat([df, curr_df], ignore_index=True)

    df.to_csv('ejecucion_familia_de_funciones.csv', index=False)
    
if __name__=="__main__":
    main()