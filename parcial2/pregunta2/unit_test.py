import unittest
from Manejador_Expresione_Aritmeticas import Manejador_Expresiones_Aritmeticas

class Test(unittest.TestCase):
    def test_manejador_vacio(self):
        try:
            manejador = Manejador_Expresiones_Aritmeticas("PRE", "")
        except:
            self.assertTrue(True)

    def test_manejador_con_orden_que_no_acepta(self):
        try:
            manejador = Manejador_Expresiones_Aritmeticas("hol", "")
        except:
            self.assertTrue(True)

        try:
            manejador = Manejador_Expresiones_Aritmeticas("", "")
        except:
            self.assertTrue(True)

    def test_manejador_correcto(self):
        manejador = Manejador_Expresiones_Aritmeticas("PRE", "9")
        manejador = Manejador_Expresiones_Aritmeticas("POST", "9 8 -")

        self.assertTrue(True)

    def test_expresion_en_orden_equivocado(self):
        try:
            manejador = Manejador_Expresiones_Aritmeticas("PRE", "9 + 8 * 7")
        except:
            self.assertTrue(True)

        try:
            manejador = Manejador_Expresiones_Aritmeticas("PRE", "9  8 + 7 *")
        except:
            self.assertTrue(True)

        try:
            manejador = Manejador_Expresiones_Aritmeticas("POST", "4+5+2")
        except:
            self.assertTrue(True)

        try:
            manejador = Manejador_Expresiones_Aritmeticas("POST", "+ 4 * 10 8")
        except:
            self.assertTrue(True)
    
    def test_expresiones_incompletas(self):
        try:
            manejador = Manejador_Expresiones_Aritmeticas("PRE", "+ 4 * 7")
        except:
            self.assertTrue(True)

        try:
            manejador = Manejador_Expresiones_Aritmeticas("POST", "4 *")
        except:
            self.assertTrue(True)

    def test_expresiones_simples_pre_eval(self):
        manejador = Manejador_Expresiones_Aritmeticas("PRE", "8")
        self.assertTrue(manejador.eval_expresion() == 8)

        manejador = Manejador_Expresiones_Aritmeticas("PRE", "+ 8 2")
        self.assertTrue(manejador.eval_expresion() == 10)

        manejador = Manejador_Expresiones_Aritmeticas("PRE", "* 8 2")
        self.assertTrue(manejador.eval_expresion() == 16)

        manejador = Manejador_Expresiones_Aritmeticas("PRE", "/ 8 2")
        self.assertTrue(manejador.eval_expresion() == 4)

        manejador = Manejador_Expresiones_Aritmeticas("PRE", "/ 2 8")
        self.assertTrue(manejador.eval_expresion() == 0)

        manejador = Manejador_Expresiones_Aritmeticas("PRE", "- 8 2")
        self.assertTrue(manejador.eval_expresion() == 6)

        manejador = Manejador_Expresiones_Aritmeticas("PRE", "- 2 8")
        self.assertTrue(manejador.eval_expresion() == -6)

        manejador = Manejador_Expresiones_Aritmeticas("PRE", "+ 8 -8")
        self.assertTrue(manejador.eval_expresion() == 0)

        manejador = Manejador_Expresiones_Aritmeticas("PRE", "* 10000000 0")
        self.assertTrue(manejador.eval_expresion() == 0)

        try:
            manejador = Manejador_Expresiones_Aritmeticas("PRE", "/ 10000000 0")
        except:
            self.assertTrue(manejador.eval_expresion() == 0)
    
    def test_expresiones_simples_post_eval(self):
        manejador = Manejador_Expresiones_Aritmeticas("POST", "8")
        self.assertTrue(manejador.eval_expresion() == 8)

        manejador = Manejador_Expresiones_Aritmeticas("POST", "8 2 +")
        self.assertTrue(manejador.eval_expresion() == 10)

        manejador = Manejador_Expresiones_Aritmeticas("POST", "8 2 *")
        self.assertTrue(manejador.eval_expresion() == 16)

        manejador = Manejador_Expresiones_Aritmeticas("POST", "8 2 /")
        self.assertTrue(manejador.eval_expresion() == 4)

        manejador = Manejador_Expresiones_Aritmeticas("POST", "2 8 /")
        self.assertTrue(manejador.eval_expresion() == 0)

        manejador = Manejador_Expresiones_Aritmeticas("POST", "8 2 -")
        self.assertTrue(manejador.eval_expresion() == 6)

        manejador = Manejador_Expresiones_Aritmeticas("POST", "2 8 -")
        self.assertTrue(manejador.eval_expresion() == -6)

        manejador = Manejador_Expresiones_Aritmeticas("POST", "8 -8 +")
        self.assertTrue(manejador.eval_expresion() == 0)

        manejador = Manejador_Expresiones_Aritmeticas("POST", "10000000 0 *")
        self.assertTrue(manejador.eval_expresion() == 0)

        try:
            manejador = Manejador_Expresiones_Aritmeticas("PRE", "10000000 0 /")
        except:
            self.assertTrue(True)

    def test_expresiones_complejas_pre_eval(self):
        manejador = Manejador_Expresiones_Aritmeticas("PRE", "+ 3 - 5 6")
        self.assertTrue(manejador.eval_expresion() == 2)
        
        manejador = Manejador_Expresiones_Aritmeticas("PRE", "* 3 + 3 - 5 6")
        self.assertTrue(manejador.eval_expresion() == 6)

        manejador = Manejador_Expresiones_Aritmeticas("PRE", "* 3 + 3 * 5 - 5 6")
        self.assertTrue(manejador.eval_expresion() == -6)

        manejador = Manejador_Expresiones_Aritmeticas("PRE", "/ 2 * 3 + 3 * 5 - 5 6")
        self.assertTrue(manejador.eval_expresion() == -1)

        manejador = Manejador_Expresiones_Aritmeticas("PRE", "* -8 + 3 - 9 5")
        self.assertTrue(manejador.eval_expresion() == -56)

        manejador = Manejador_Expresiones_Aritmeticas("PRE", "* -8 + 3 - 9 5")
        self.assertTrue(manejador.eval_expresion() == -56)

        manejador = Manejador_Expresiones_Aritmeticas("PRE", "/ 72 * 9 8")
        self.assertTrue(manejador.eval_expresion()==1)

    def test_expresiones_complejas_post_eval(self):
        manejador = Manejador_Expresiones_Aritmeticas("POST", "4 5 + 9 -")
        self.assertTrue(manejador.eval_expresion() == 0)

        manejador = Manejador_Expresiones_Aritmeticas("POST", "4 5 + 9 - -18 +")
        self.assertTrue(manejador.eval_expresion() == -18)
        
        manejador = Manejador_Expresiones_Aritmeticas("POST", "4 5 + 9 - -18 + -1 *")
        self.assertTrue(manejador.eval_expresion() == 18)

        manejador = Manejador_Expresiones_Aritmeticas("POST", "4 5 + 9 - -18 + -1 * 2 /")
        self.assertTrue(manejador.eval_expresion() == 9)

        manejador = Manejador_Expresiones_Aritmeticas("POST", "4 5 + 9 - -18 + -1 * 18 -")
        self.assertTrue(manejador.eval_expresion() == 0)

        manejador = Manejador_Expresiones_Aritmeticas("POST", "4 5 + 9 - -18 + -1 *")
        self.assertTrue(manejador.eval_expresion() == 18)
        
        manejador = Manejador_Expresiones_Aritmeticas("POST", "4 5 + 9 - -18 + -1 * 18 +")
        self.assertTrue(manejador.eval_expresion() == 36)

    def test_expresion_infija_pre(self):
        manejador = Manejador_Expresiones_Aritmeticas("PRE", "4")
        self.assertTrue(manejador.expresion_infija() == "4")

        manejador = Manejador_Expresiones_Aritmeticas("PRE", "+ 4 4")
        self.assertTrue(manejador.expresion_infija() == "(4 + 4)")

        manejador = Manejador_Expresiones_Aritmeticas("PRE", "- 5 + 4 4")
        self.assertTrue(manejador.expresion_infija() == "5 - (4 + 4)")

        manejador = Manejador_Expresiones_Aritmeticas("PRE", "+ * + 3 4 5 7")
        self.assertTrue(manejador.expresion_infija() == "(3 + 4) * 5 + 7")

    def test_expresion_infija_post(self):
        manejador = Manejador_Expresiones_Aritmeticas("POST", "4")
        self.assertTrue(manejador.expresion_infija() == "4")

        manejador = Manejador_Expresiones_Aritmeticas("POST", "4 4 +")
        self.assertTrue(manejador.expresion_infija() == "(4 + 4)")

        manejador = Manejador_Expresiones_Aritmeticas("POST", "4 4 + 5 -")
        self.assertTrue(manejador.expresion_infija() == "(4 + 4) - 5")

        manejador = Manejador_Expresiones_Aritmeticas("POST", "8 3 - 8 4 4 + * +")
        self.assertTrue(manejador.expresion_infija() == "(8 - 3) + 8 * (4 + 4)")

if __name__ == "__main__":
    unittest.main()
