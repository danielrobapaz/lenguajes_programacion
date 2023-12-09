import unittest
from Tabla_de_metodos import Tabla_de_metodos


class Test(unittest.TestCase):
    def test_manejador_vacio(self):
        manejador = Tabla_de_metodos()
        self.assertEqual(manejador.tabla, {})

    def test_agregar_tipo_sin_metodos(self):
        manejador = Tabla_de_metodos()
        self.assertTrue(manejador.agregar_clase('A', []))
        self.assertTrue(manejador.describir('A') == [])

    def test_agregar_tipo_con_metodos(self):
        manejador = Tabla_de_metodos()
        self.assertTrue(manejador.agregar_clase('A', ['a', 'b', 'c']))
        self.assertTrue(manejador.describir('A')==[('a', 'A'), ('b', 'A'), ('c', 'A')])

    def test_agregar_varios_tipos(self):
        manejador = Tabla_de_metodos()
        self.assertTrue(manejador.agregar_clase('A', ['a', 'b', 'c']))
        self.assertTrue(manejador.agregar_clase('B', ['a', 'b', 'c']))

        self.assertTrue(manejador.describir('A')==[('a', 'A'), ('b', 'A'), ('c', 'A')])
        self.assertTrue(manejador.describir('B')==[('a', 'B'), ('b', 'B'), ('c', 'B')])

    def test_agregar_tipos_repetidos(self):
        manejador = Tabla_de_metodos()
        self.assertTrue(manejador.agregar_clase('A', ['a', 'b', 'c']))
        self.assertFalse(manejador.agregar_clase('A', []))

    def test_agregar_clase_con_metodos_repetidos(self):
        manejador = Tabla_de_metodos()
        self.assertFalse(manejador.agregar_clase('A', ['a', 'a', 'b', 'c']))

    def test_agregar_super_no_existente(self):
        manejador = Tabla_de_metodos()
        self.assertFalse(manejador.agregar_clase('A', ['a', 'b', 'c'], 'B'))

    def test_describir_clase_no_existe(self):
        manejador = Tabla_de_metodos()
        self.assertIsNone(manejador.describir('A'))

    def test_agregar_herencia_un_nivel_sin_solapamiento(self):
        manejador = Tabla_de_metodos()
        self.assertTrue(manejador.agregar_clase('A', ['a', 'b', 'c']))
        self.assertTrue(manejador.agregar_clase('B', ['d', 'e', 'f'], 'A'))

        self.assertTrue(manejador.describir('B') == [('d', 'B'), ('e', 'B'), ('f', 'B'), 
                                                     ('a', 'A'), ('b', 'A'), ('c', 'A')])
    
    def test_agregar_herencia_un_nivel_con_solapamiento(self):
        manejador = Tabla_de_metodos()
        self.assertTrue(manejador.agregar_clase('A', ['a', 'b', 'c']))
        self.assertTrue(manejador.agregar_clase('B', ['d', 'c', 'a'], 'A'))

        self.assertTrue(manejador.describir('B') == [('d', 'B'), ('c', 'B'), ('a', 'B'), ('b', 'A')])

    def test_agregar_herencia_un_nivel_sobreescribir_metodos(self):
        manejador = Tabla_de_metodos()
        self.assertTrue(manejador.agregar_clase('A', ['a', 'b', 'c']))
        self.assertTrue(manejador.agregar_clase('B', ['b', 'c', 'a'], 'A'))

        self.assertTrue(manejador.describir('B') == [('b', 'B'), ('c', 'B'), ('a', 'B')])

    def test_agregar_herencia_dos_niveles_sin_solapamiento(self):
        manejador = Tabla_de_metodos()
        self.assertTrue(manejador.agregar_clase('A', ['a','b','c']))
        self.assertTrue(manejador.agregar_clase('B', ['d','e','f'], 'A'))
        self.assertTrue(manejador.agregar_clase('C', ['g','h','i'], 'B'))

        self.assertTrue(manejador.describir('C')==[('g', 'C'), ('h', 'C'), ('i', 'C'), 
                                                   ('d', 'B'), ('e', 'B'), ('f', 'B'), 
                                                   ('a', 'A'), ('b', 'A'), ('c', 'A')])
        
    def test_agregar_herencia_dos_niveles_con_solapamiento(self):
        manejador = Tabla_de_metodos()
        self.assertTrue(manejador.agregar_clase('A', ['a','b','c']))
        self.assertTrue(manejador.agregar_clase('B', ['d','a','f'], 'A'))
        self.assertTrue(manejador.agregar_clase('C', ['d','h','a'], 'B'))

        self.assertTrue(manejador.describir('C')==[('d', 'C'), ('h', 'C'), ('a', 'C'), 
                                                   ('f', 'B'), 
                                                   ('b', 'A'), ('c', 'A')])

    def test_agregar_herencia_dos_niveles_sobreescribir_metodos(self):
        manejador = Tabla_de_metodos()
        self.assertTrue(manejador.agregar_clase('A', ['a','b','c']))
        self.assertTrue(manejador.agregar_clase('B', ['d','e','f'], 'A'))
        self.assertTrue(manejador.agregar_clase('C', ['a','b','c', 'd', 'e', 'f'], 'B'))

        self.assertTrue(manejador.describir('C')==[('a', 'C'), ('b', 'C'), ('c', 'C'), 
                                                   ('d', 'C'), ('e', 'C'), ('f', 'C')])
        
    def test_herencia_clase_vacia(self):
        manejador = Tabla_de_metodos()
        self.assertTrue(manejador.agregar_clase('A', ['a', 'b', 'c']))
        self.assertTrue(manejador.agregar_clase('B', [], 'A'))

        self.assertTrue(manejador.describir('B')==[('a', 'A'), ('b', 'A'), ('c', 'A')])

    def test_herencia_super_vacia(self):
        manejador = Tabla_de_metodos()
        self.assertTrue(manejador.agregar_clase('A', []))
        self.assertTrue(manejador.agregar_clase('B', ['a', 'b', 'c'], 'A'))

        self.assertTrue(manejador.describir('B')==[('a', 'B'), ('b', 'B'), ('c', 'B')])

if __name__ == "__main__":
    unittest.main()