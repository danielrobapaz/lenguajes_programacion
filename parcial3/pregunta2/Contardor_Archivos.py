import os
import threading

class Contador_Archivos:
    def __init__(self, path: str):
        self.path = path
        if not os.path.isdir(path):
            raise Exception("La direccion dada no es un directorio")
        self.numero_archivos = 0
        self.__contar()

    def __contar(self):
        def contar_hilo(path: str, return_value: [None]):
            for item in os.listdir(path):
                if os.path.isfile(os.path.join(path, item)):
                    with mutex:
                        return_value[0] += 1

                elif os.path.isdir(os.path.join(path, item)):
                    thread = threading.Thread(target=contar_hilo, args=(os.path.join(path, item), return_value))
                    thread.start()
                    thread.join()

        mutex = threading.Lock()
        numero_archivos = [0]
        thread = threading.Thread(target=contar_hilo, args=(self.path,numero_archivos))
        thread.start()
        thread.join()

        self.numero_archivos = numero_archivos[0]

    def obtener_numero_archivos(self) -> int:
        return self.numero_archivos
    

contador = Contador_Archivos('/home/daniel/Documents/Trimestre/Lenguajes/lenguajes_programacion/parcial3')
print(contador.obtener_numero_archivos())