"""
Programa de pruebas unitarias automatizadas para la clase T_Diagrams

Autor: Daniel Robayo
Carnet: 18-11086
Lenguajes de programcion CI-3641
"""

import unittest
from diagramas import T_Diagrams

class Tests(unittest.TestCase):
    def test_LoadProgram(self):
        diag = T_Diagrams()
        diag.add_program('prog1', 'java')
        
        self.assertEqual(diag.programs, [{'name':'prog1', 'leng':'java'}])
                         
                         
    def test_LoadInterpreter(self):
        diag = T_Diagrams()
        diag.add_interpreter('java', 'c')

        self.assertEqual(diag.interpreters, [{'base_leng':'java', 'leng_to':'c'}])
    
    def test_LoadTraductolue(self):
        diag = T_Diagrams()
        diag.add_translator('java', 'c', 'python')

        self.assertEqual(diag.translators, [{'base_leng':'java', 
                                             'leng_from':'c', 'leng_to':'python'}])
        
    def test_ExcecuteNonExistingProgram(self):
        diag = T_Diagrams()
        
        self.assertFalse(diag.can_excute('hola'))

    def test_ExecuteLocalProgram(self):
        diag = T_Diagrams()

        diag.add_program('prog1', 'LOCAL')
        self.assertTrue(diag.can_excute('prog1'))
    
    def test_ExecuteProgramWithInterpreter(self):
        diag = T_Diagrams()
        diag.add_program('prog1', 'java')

        self.assertFalse(diag.can_excute('prog1'))
        
        diag.add_interpreter('LOCAL', 'java')
        
        self.assertTrue(diag.can_excute('prog1'))

    def test_ExecuteProgramWithTwoInterpreters(self):
        diag = T_Diagrams()
        diag.add_program('prog1', 'python')
        diag.add_interpreter('LOCAL', 'java')
        diag.add_interpreter('java', 'python')

        self.assertTrue(diag.can_excute('prog1'))

    def test_ExcecuteAProgramWithTraductor(self):
        diag = T_Diagrams()
        diag.add_program('prog1', 'python')
        diag.add_translator('LOCAL', 'python', 'LOCAL')

        self.assertTrue(diag.can_excute('prog1'))

    def test_ExceuteAProgramWithInterpreterTraductor(self):
        diag = T_Diagrams()
        diag.add_program('prog1', 'python')
        diag.add_translator('java', 'python', 'LOCAL')
        diag.add_interpreter('LOCAL', 'java')

        self.assertTrue(diag.can_excute('prog1'))

    def test_ComplexDiagram(self):
        diag = T_Diagrams()
        diag.add_program('prog1', 'python')
        diag.add_interpreter('java', 'python')
        diag.add_translator('cpp', 'java', 'c')
        diag.add_interpreter('c', 'java')
        diag.add_interpreter('LOCAL', 'java')

        self.assertTrue(diag.can_excute('prog1'))
    
    def test_PascalPcode(self):
        diag = T_Diagrams()
        diag.add_program('prog1', 'pascal')

        # niklaus distribuia pascal con
        diag.add_translator('pascal', 'pascal', 'pcode')
        diag.add_translator('pcode', 'pascal', 'pcode')
        diag.add_interpreter('pascal', 'pcode')

        #el usuario debia traducir el interprete a su maquina lical
        diag.add_interpreter('LOCAL', 'pcode')

        # se puede ejecutar pascal sobre pcode
        self.assertTrue(diag.can_excute('prog1'))

        
if __name__ == "__main__":
    unittest.main()