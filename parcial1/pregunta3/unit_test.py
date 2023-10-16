import unittest
from buddy_system import Buddy_System

class Tests(unittest.TestCase):
    def test_CreateBuddySystem(self):
        bd = Buddy_System(18)

        self.assertEqual(bd.total_blocks, 16, 'Error en calculo de bloques')
        self.assertEqual(bd.empty_blocks[16], 1, 'Bloque inicial de tamano equivocado')

    def test_ReserveEntireBlock(self):
        bd = Buddy_System(32)

        bd.reserve('proc', 32)
        self.assertEqual(bd.empty_blocks, {}, 'Mala asignacion de bloque entero')
        
        bd = Buddy_System(32)
        bd.reserve('proc', 17)
        self.assertEqual(bd.empty_blocks, {}, 'Mala asignacion de bloque entero')

    def test_ReserveTwoBlocksSameSize(self):
        bd = Buddy_System(32)

        bd.reserve('proc1', 15)
        bd.reserve('proc2', 15)

        self.assertEqual(len(bd.assigned_blocks[16]), 2, 'Error asignando bloques de igual tamano')


    def test_ReserveTwoBlocksDiffSize(self):
        bd = Buddy_System(32)
        
        bd.reserve('proc1', 4)
        bd.reserve('proc2', 3)

        self.assertEqual(bd.empty_blocks, {8:1, 16:1}, 'Error asignando bloques de tamano distinto')
        self.assertEqual(len(bd.assigned_blocks[4]), 2, 'Error asignando bloques de tamano distinto')
    
    def test_ReserveThreeBlocksDiffSize(self):
        bd = Buddy_System(32)

        bd.reserve('proc1', 3)
        bd.reserve('proc2', 16)
        bd.reserve('proc3', 1)
    
        self.assertEqual(bd.empty_blocks, {1: 1, 2: 1, 16: 1}, 'Error asignado bloques de tamano distinto')
    
    def test_FreeOne(self):
        bd = Buddy_System(32)

        bd.reserve('proc1', 16)
        bd.free('proc1')

        self.assertEqual(bd.empty_blocks, {32:1}, 'Error liberando bloque')
        self.assertEqual(bd.assigned_blocks, {}, 'Error liberando bloque')

    def test_FreeAndJointOne(self):
        bd = Buddy_System(32)

        bd.reserve('proc1', 16)
        bd.reserve('proc2', 16)
        bd.free('proc1')

        self.assertEqual(bd.empty_blocks, {16:1}, 'Error liberando bloque')

        bd.free('proc2')

        self.assertEqual(bd.empty_blocks, {32:1}, 'Error liberando bloque')

    def test_ReserveSameProccess(self):
        bd = Buddy_System(16)

        bd.reserve('proc1', 1)
        prev = bd.empty_blocks
        bd.reserve('proc1', 16)

        self.assertEqual(prev, bd.empty_blocks, 'Error asignando bloque a mismo proceso')

    def test_ReserveABiggerProc(self):
        bd = Buddy_System(16)

        bd.reserve('proc1', 100)
        self.assertEqual(bd.empty_blocks, {}, 'Error asignando un bloque que no cabe')

    def test_FreeAProccesNotAssigned(self):
        bd = Buddy_System(32)
        
        bd.reserve('proc1', 4)
        prev = bd.empty_blocks
        bd.free('proc2')

        self.assertEqual(bd.empty_blocks, prev, 'Error liberando proceso de tamano que no existe')

if __name__ == '__main__':
    unittest.main()