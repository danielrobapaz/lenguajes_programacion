import unittest
from Manejador_De_Tipos_De_Datos import Manejador_De_Tipos_De_Datos

class Test(unittest.TestCase):
    def test_agregar_tipo_atomicos(self):
        manejador = Manejador_De_Tipos_De_Datos()
        
        self.assertTrue(manejador.agregar_atomico("char", 4, 8))
        self.assertFalse(manejador.agregar_atomico("char", 2, 3))

        (res, descripcion) = manejador.describir("char")

        self.assertTrue(descripcion['sin_empaquetado'] == [4, 8, 0])
        self.assertTrue(descripcion['empaquetado'] ==  [4, 8, 0])
        self.assertTrue(descripcion['optimo'] == [4, 8, 0])

    def test_agregar_registro(self):
        manejador = Manejador_De_Tipos_De_Datos()

        self.assertTrue(manejador.agregar_atomico("char", 3, 2))
        self.assertTrue(manejador.agregar_atomico("super char", 5, 2))
        self.assertTrue(manejador.agregar_atomico("mega char", 7, 2))
        self.assertTrue(manejador.agregar_registro("struct", ["char", "super char", "mega char"]))

        (res, descripcion) = manejador.describir("struct")

        self.assertTrue(descripcion['sin_empaquetado'] == [17, 20, 2])
        self.assertTrue(descripcion['empaquetado'] == [15, 16, 0])
        self.assertTrue(descripcion['optimo'] == [17, 20, 2])

    def test_agregar_union(self):
        manejador = Manejador_De_Tipos_De_Datos()

        self.assertTrue(manejador.agregar_atomico("char", 3, 2))
        self.assertTrue(manejador.agregar_atomico("super char", 5, 2))
        self.assertTrue(manejador.agregar_atomico("mega char", 7, 2))
        self.assertTrue(manejador.agregar_registro("struct", ["char", "super char", "mega char"]))
        self.assertTrue(manejador.agregar_variante("union", ["mega char", "struct", "mega char"]))

        (res, descripcion_union) = manejador.describir("union")
        (res, descripcion_struct) = manejador.describir("struct")

        self.assertTrue(descripcion_union['sin_empaquetado'] == descripcion_struct['sin_empaquetado'])
        self.assertTrue(descripcion_union['empaquetado'] == descripcion_struct['empaquetado'])
        self.assertTrue(descripcion_union['optimo'] == descripcion_struct['optimo'])

    def test_agregar_union_1(self):
        manejador = Manejador_De_Tipos_De_Datos()
        
        self.assertTrue(manejador.agregar_atomico("char", 3, 2))
        self.assertTrue(manejador.agregar_atomico("super char", 5, 2))
        self.assertTrue(manejador.agregar_atomico("mega char", 7, 2))
        self.assertTrue(manejador.agregar_atomico("super tipo", 100, 1))
        self.assertTrue(manejador.agregar_registro("struct", ["char", "super char", "mega char", "mega char"]))
        self.assertTrue(manejador.agregar_variante("union", ["mega char", "struct", "mega char", "super tipo"]))

        (res, descripcion) = manejador.describir("union")

        self.assertTrue(descripcion['sin_empaquetado'] == [100, 28, 0])
        self.assertTrue(descripcion['empaquetado'] == [100, 24, 0])
        self.assertTrue(descripcion['optimo'] == [100, 28, 0])
        

    def test_struct_struct(self):
        manejador = Manejador_De_Tipos_De_Datos()
        
        self.assertTrue(manejador.agregar_atomico("char", 3, 2))
        self.assertTrue(manejador.agregar_atomico("super char", 5, 2))
        self.assertTrue(manejador.agregar_atomico("mega char", 7, 2))
        
        self.assertTrue(manejador.agregar_registro("struct", ["char", "char", "char"]))
        self.assertTrue(manejador.agregar_registro("super struct", ["super char", "super char", "super char"]))
        self.assertTrue(manejador.agregar_registro("mega struct", ["mega char", "mega char", "mega char"]))

        self.assertTrue(manejador.agregar_registro("super mega struct", ["struct", "super struct", "mega struct"]))

        (res, descripcion) = manejador.describir("super mega struct")
        
        self.assertTrue(descripcion['sin_empaquetado'] == [71, 72, 20])
        self.assertTrue(descripcion['empaquetado'] == [45, 48, 0])
        self.assertTrue(descripcion['optimo'] == [57, 60, 6])

    def test_struct_struct(self):
        manejador = Manejador_De_Tipos_De_Datos()
        
        self.assertTrue(manejador.agregar_atomico("char", 3, 2))
        self.assertTrue(manejador.agregar_atomico("super char", 5, 2))
        self.assertTrue(manejador.agregar_atomico("mega char", 7, 2))
        
        self.assertTrue(manejador.agregar_registro("struct", ["char", "char", "char"]))
        self.assertTrue(manejador.agregar_registro("super struct", ["super char", "super char", "super char"]))
        self.assertTrue(manejador.agregar_registro("mega struct", ["mega char", "mega char", "mega char"]))

        self.assertTrue(manejador.agregar_variante("super mega union", ["struct", "super struct", "mega struct"]))

        (res, descripcion) = manejador.describir("super mega union")
        
        self.assertTrue(descripcion['sin_empaquetado'] == [23, 120, 2])
        self.assertTrue(descripcion['empaquetado'] == [21, 48, 0])
        self.assertTrue(descripcion['optimo'] == [23, 120, 2])

    def test_struct_vacio(self):
        manejador = Manejador_De_Tipos_De_Datos()
        self.assertFalse(manejador.agregar_registro("soy vacio", []))

    def test_variante_vacio(self):
        manejador = Manejador_De_Tipos_De_Datos()
        self.assertFalse(manejador.agregar_variante("soy vacio", []))

    def test_agregar_tipo_repetidos(self):
        manejador = Manejador_De_Tipos_De_Datos()
        
        self.assertTrue(manejador.agregar_atomico("char", 3, 2))
        self.assertTrue(manejador.agregar_atomico("super char", 5, 2))
        self.assertTrue(manejador.agregar_atomico("mega char", 7, 2))
        self.assertTrue(manejador.agregar_registro("struct", ["char", "char", "char"]))
        self.assertTrue(manejador.agregar_registro("super struct", ["super char", "super char", "super char"]))
        self.assertTrue(manejador.agregar_registro("mega struct", ["mega char", "mega char", "mega char"]))
        self.assertTrue(manejador.agregar_variante("super mega union", ["struct", "super struct", "mega struct"]))

        self.assertFalse(manejador.agregar_atomico("struct", 4, 5))
        self.assertFalse(manejador.agregar_registro("char", ["char", "char"]))
        self.assertFalse(manejador.agregar_variante("super mega union", ["char", "struct"]))

    def test_agregar_tipo_no_existen(self):
        manejador = Manejador_De_Tipos_De_Datos()

        self.assertTrue(manejador.agregar_atomico("char", 3, 2))
        self.assertTrue(manejador.agregar_atomico("super char", 5, 2))
        self.assertTrue(manejador.agregar_atomico("mega char", 7, 2))
        self.assertTrue(manejador.agregar_registro("struct", ["char", "char", "char"]))

        self.assertFalse(manejador.agregar_registro("struct", ["int", "char", "float"]))
        self.assertFalse(manejador.agregar_variante("union", ["struct", "char", "float"]))
    
    def test_clase(self):
        manejador = Manejador_De_Tipos_De_Datos()

        self.assertTrue(manejador.agregar_atomico("bool", 1, 2))
        self.assertTrue(manejador.agregar_atomico("char", 2, 2))
        self.assertTrue(manejador.agregar_atomico("int", 4, 4))
        self.assertTrue(manejador.agregar_atomico("double", 8, 8))
        self.assertTrue(manejador.agregar_registro("meta", ["int", "char", "int", "double", "bool"]))

        (res, descripcion) = manejador.describir("meta")
        
        self.assertTrue(descripcion['sin_empaquetado'] == [25, 28, 6])
        self.assertTrue(descripcion['empaquetado'] == [19, 20, 0])
        self.assertTrue(descripcion['optimo'] == [19, 20, 0])

if __name__ == "__main__":
    unittest.main()