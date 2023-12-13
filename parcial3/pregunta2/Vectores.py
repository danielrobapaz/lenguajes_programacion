import threading
from random import randint
import numpy as np
import time

class Vector:
    def __init__(self, elementos: [float]): 
        if len(elementos) < 1:
            raise Exception("No se pueden definir vectores con menos de una dimension")
        self.coordenadas = np.array(elementos)
        self.tamano = len(elementos)

    def obtener_tamano(self) -> int:
        return self.tamano

    def obtener_coordenadas(self) -> [float]:
        return self.coordenadas
    

    def producto_punto(self, otro_vector) -> float:
        if self.obtener_tamano() != otro_vector.obtener_tamano():
            raise Exception("El producto punto requiere de vectores de igual dimension")
        
        estas_coordenadas = self.obtener_coordenadas()
        otras_coordeandas = otro_vector.obtener_coordenadas()
        if self.obtener_tamano() < 5:
            return np.dot(estas_coordenadas, otras_coordeandas)
        
        def mini_producto_punto(segmento1: np.array,
                                segmento2: np.array,
                                n_hilo: int,
                                return_value: list):
            return_value[0] =  np.dot(segmento1, segmento2)

        [segmento_1, segmento_2, segmento_3, segmento_4] = np.array_split(estas_coordenadas, 4)
        [otro_segmento_1, otro_segmento_2, otro_segmento_3, otro_segmento_4] = np.array_split(otras_coordeandas, 4)

        return_thread_1 = [None]
        return_thread_2 = [None]
        return_thread_3 = [None]
        return_thread_4 = [None]

        thread_1 = threading.Thread(target=mini_producto_punto, args=(segmento_1, otro_segmento_1, 1, return_thread_1))
        thread_2 = threading.Thread(target=mini_producto_punto, args=(segmento_2, otro_segmento_2, 2, return_thread_2))
        thread_3 = threading.Thread(target=mini_producto_punto, args=(segmento_3, otro_segmento_3, 3, return_thread_3))
        thread_4 = threading.Thread(target=mini_producto_punto, args=(segmento_4, otro_segmento_4, 4, return_thread_4))
        
        thread_1.start()
        thread_2.start()
        thread_3.start()
        thread_4.start()

        thread_1.join()
        thread_2.join()
        thread_3.join()
        thread_4.join()

        return return_thread_1[0] + return_thread_2[0] + return_thread_3[0] + return_thread_4[0]