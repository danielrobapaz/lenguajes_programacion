class Tabla_de_metodos():
    def __init__(self):
        self.tabla = {}


    def agregar_clase(self,
                      tipo: str,
                      metodos: [str],
                      super: str = None) -> bool:
        if tipo in self.tabla:
            return False
        
        if len(metodos) != len(set(metodos)):
            return False
        
        if super:
            if not super in self.tabla:
                return False
            
            metodos_super = self.tabla[super]
            metodos_tipo = [(n, tipo) for n in metodos]

            for (m,t) in metodos_super:
                if not m in metodos:
                    metodos_tipo.append((m,t))
            self.tabla[tipo] = metodos_tipo            
        else:
            self.tabla[tipo] = [(n, tipo) for n in metodos]
        return True

    def describir(self, tipo:str) -> [(str, str)]:
        if tipo in self.tabla:
            return self.tabla[tipo]