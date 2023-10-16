"""
Implementacion de la clase que maneja los diagramas T.

Se tienen 4 operaciones
    - Agregar programa
    - Agregar interprete
    - Agregar traductor
    - Verificar si se puede ejecutar un programa

Autor: Daniel Robayo
Carnet: 18-11086

Lenguajes de programacion CI-3641
"""

class T_Diagrams():
    def __init__(self):
        self.programs = []
        self.interpreters = []
        self.translators = []

    """
        Dado un nombre de un programa y el lenguaje en el que esta escrito,
        agrega el programa junto con su lenguaje al manejador

        Retorna: 
            True si se puede agregar
            False si ya existe un programa con el mismo nombre
    """
    def add_program(self, name, leng):
        if any(p['name']==name for p in self.programs):
            print(f"Ya existe un ese programa")
            return False
        
        self.programs.append({'name':name, 'leng':leng})
        return True
    
    """
        Dado un lenguaje base y un lenguaje destino, agrega un interpretador del lenguaje destino
        escrito en el lenguaje base.

        Retorna:
            True si se puee agregar
            False si ya existe un interprete con los mismo lenguajes.
    """
    def add_interpreter(self, base_leng, leng_to):
        if any(i['base_leng']==base_leng and i['leng_to']==leng_to for i in self.interpreters):
            print("Ya existe ese interpretador")
            return False
        
        self.interpreters.append({'base_leng':base_leng, 'leng_to':leng_to})
        return True
    
    """
        Dado un lenguaje base, un lenguaje origen y otro destino, agrega un interpretador
        desde el lenguaje origen al lenguaje destino escrito en el lenguaje base

        Retorna:
            True si se puede agregar
            False si ya existe el mismo traductor
    """
    def add_translator(self, base_leng, leng_from, leng_to):
        if any(t['base_leng']==base_leng and t['leng_from']==leng_from and t['leng_to']==leng_to for t in self.translators):
            print('Ya existe ese traductor')
            return False

        self.translators.append({'base_leng':base_leng, 'leng_from':leng_from, 'leng_to':leng_to})
        return True
    
    """
        Verifica si se puede ejecutar un programa con un nombre dado.

        Para esto se obtiene una lista de los programa que se entienden con las siguientes reglas

        - Dado un interprete de a escrito en b, si entiendo b => entiendo a
        - Dado un traductor de b hacia c escrito en a, si entiendo a y b entonces entiendo c

        Retorna:
            True si el programa se puede ejecutar
            False caso contrario o el programa no existe 
    """
    def can_excute(self, name):
        prev_excecutable = {'LOCAL'}

        while (True):
            curr_excecutable = prev_excecutable
            for i in self.interpreters:
                if i['base_leng'] in curr_excecutable:
                    curr_excecutable = curr_excecutable.union({i['leng_to']})

            for t in self.translators:
                if t['base_leng'] in curr_excecutable and t['leng_to'] in curr_excecutable:
                    curr_excecutable = curr_excecutable.union({t['leng_from']})
            
            if prev_excecutable == curr_excecutable: # chequeamos el punto fijo
                break
            
            prev_excecutable = curr_excecutable

        # buscamos el lenguaje en el que esta escrito el programa
        # si el programa no existe leng == ""
        leng = ""
        for p in self.programs:
            if p['name'] == name:
                leng = p['leng']
        
        return leng != "" and leng in prev_excecutable