from Nodo_Expresion import (de_exp_a_nodo_expresion, inorder, eval)

class Manejador_Expresiones_Aritmeticas:
    def __init__(self, orden: str, exp: str):
        if not orden in ['PRE', 'POST']:
            raise Exception("""El manejador solo maneja expressiones escritas en notacion
                            prefija 'INF' y postfija 'POST'""")
        
        if exp == '':
            raise Exception("El manejador no recibe expresiones vacias")
        
        self.expresion = de_exp_a_nodo_expresion(orden, exp)

    def eval_expresion(self):
        return eval(self.expresion)
    
    def expresion_infija(self):
        return "".join(inorder(self.expresion))