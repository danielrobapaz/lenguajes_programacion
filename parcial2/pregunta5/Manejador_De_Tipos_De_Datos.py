from itertools import permutations

class Manejador_De_Tipos_De_Datos:
    def __init__(self):
        self.tipos = {}

    def agregar_atomico(self, 
                        nombre_tipo: str, 
                        representacion: int,
                        alieanacion: int) -> bool:
        if nombre_tipo in self.tipos or alieanacion <= 0:
            return False
        
        self.tipos[nombre_tipo] = {
            'sin_empaquetado': [representacion, alieanacion, 0],
            'empaquetado': [representacion, alieanacion, 0],
            'optimo': [representacion, alieanacion, 0]
        }
        return True
    
    def agregar_registro(self, 
                         nombre_tipo: str,
                         tipos: [str]) -> bool:
        if nombre_tipo in self.tipos or not all(t in self.tipos for t in tipos):
            return False

        if tipos == []:
            return False
        
        no_empaquetado = self.__tipos_sin_empaquetado(tipos)
        empaquetado = self.__tipos_empaquetado(tipos)
        optimo = self.__tipos_optimo(tipos)

        self.tipos[nombre_tipo] = {
            'sin_empaquetado': no_empaquetado,
            'empaquetado': empaquetado,
            'optimo': optimo
        }
        return True
    
    def agregar_variante(self,
                         nombre_tipo: str,
                         tipos: [str]) -> bool:
 
        if nombre_tipo in self.tipos or not all(t in self.tipos for t in tipos):
            return False
         
        if tipos == []:
            return False
        
        no_empaquetado = self.__tipos_sin_empaquetado_max(tipos)
        empaquetado = self.__tipos_empaquetado_max(tipos)
        optimo = self.__tipos_optimo_max(tipos)

        self.tipos[nombre_tipo] = {
            'sin_empaquetado': no_empaquetado,
            'empaquetado': empaquetado,
            'optimo': optimo    
        }   

        return True
    
    def describir(self,
                  nombre_tipo: str) -> (bool, dict):
        if not nombre_tipo in self.tipos:
            return (False, {})
        
        return (True, self.tipos[nombre_tipo])
                
    def __tipos_sin_empaquetado(self,
                               tipos: [str]) -> [int, int, int]:
        mem = []
        for t in tipos:
            [curr_tamano, curr_alineacion, curr_desperdicio] = self.tipos[t]['sin_empaquetado']
            while len(mem) % curr_alineacion != 0:
                mem.append(0)
            
            for i in range(curr_tamano):
                mem.append(1)
        
        ocupado = len(mem)
        desperdiciado = ocupado - sum(1 for m in mem if m==1)
        alineacion = ocupado + (4 - ocupado % 4)
        return [ocupado, alineacion, desperdiciado]
    
    def __tipos_empaquetado(self,
                            tipos: [str]) -> [int, int, int]:
        ocupado = sum(self.tipos[t]['empaquetado'][0] for t in tipos)
        desperdiciado = 0
        alineacion = ocupado + (4 - ocupado % 4)
        return [ocupado, alineacion, desperdiciado]
    
    def __tipos_optimo(self,
                       tipos: [str]) -> [int, int, int]:
        todos_tipos = list(permutations(tipos, len(tipos)))

        ocupado_optimo = float('inf')
        alineacion_optimo = float('inf')
        desperdicio_optimo = float('inf')

        for t in todos_tipos:
            [curr_ocupado, curr_alineacion, curr_desperdicio] = self.__tipos_sin_empaquetado(t)

            if curr_ocupado < ocupado_optimo:
                ocupado_optimo = curr_ocupado
                alineacion_optimo = curr_alineacion
                desperdicio_optimo = curr_desperdicio

        return [ocupado_optimo, alineacion_optimo, desperdicio_optimo]
    
    def __tipos_sin_empaquetado_max(self,
                                    tipos: [str]) -> [int, int, int]:
        ocupado_mayor = float('-inf')
        alineacion_mayor = []
        desperdicio_mayor = float('-inf')

        for t in tipos:
            [curr_ocupado, curr_alineacion, curr_desperdicio] = self.tipos[t]['sin_empaquetado']
            if ocupado_mayor < curr_ocupado:
                ocupado_mayor = curr_ocupado
                alineacion_mayor.append(curr_alineacion)
                desperdicio_mayor = curr_desperdicio

        return [ocupado_mayor, mcm(alineacion_mayor), desperdicio_mayor]
    
    def __tipos_empaquetado_max(self,
                                    tipos: [str]) -> [int, int, int]:
        ocupado_mayor = float('-inf')
        alineacion_mayor = []
        desperdicio_mayor = float('-inf')

        for t in tipos:
            [curr_ocupado, curr_alineacion, curr_desperdicio] = self.tipos[t]['empaquetado']

            if ocupado_mayor < curr_ocupado:
                ocupado_mayor = curr_ocupado
                alineacion_mayor.append(curr_alineacion)
                desperdicio_mayor = curr_desperdicio

        return [ocupado_mayor, mcm(alineacion_mayor), desperdicio_mayor]
    
    def __tipos_optimo_max(self,
                            tipos: [str]) -> [int, int, int]:
        ocupado_mayor = float('-inf')
        alineacion_mayor = []
        desperdicio_mayor = float('-inf')

        for t in tipos:
            [curr_ocupado, curr_alineacion, curr_desperdicio] = self.tipos[t]['optimo']

            if ocupado_mayor < curr_ocupado:
                ocupado_mayor = curr_ocupado
                alineacion_mayor.append(curr_alineacion)
                desperdicio_mayor = curr_desperdicio

        return [ocupado_mayor, mcm(alineacion_mayor), desperdicio_mayor]

def mcd(a: int, b: int) -> int:
    if (a == 0):
        return b
    return mcd(b % a, a)

def mcm(lista: [int], index: int=0) -> int:
    if (index == len(lista)-1):
        return lista[index]
    
    a = lista[index]
    b = mcm(lista, index+1)
    return int(a*b/mcd(a, b))