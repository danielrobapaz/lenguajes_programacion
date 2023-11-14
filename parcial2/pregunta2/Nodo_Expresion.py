from collections import deque

def es_operador(c: str):
    return c in ['+', '-', '*', '/']

class Nodo_Expresion:
        def __init__(self, opr, nodo_izq = None, nodo_der = None) -> None:
            if type(opr) == str and not opr in ['+', '-', '*', '/']:
                raise Exception("""El manejador acepta +, -, * y /""")
            self.val = opr # puede ser entero o un operador
            self.nodo_izq = nodo_izq
            self.nodo_der = nodo_der
                
def de_exp_a_nodo_expresion(orden: str, exp: str) -> Nodo_Expresion:
    exp_extend = exp.split(' ')
    exp_extend = [item for item in exp_extend if item != '']
    if orden == 'PRE':
        exp_extend.reverse()
    s = deque()
    for c in exp_extend:
        if es_operador(c):
            operando_der, operando_izq = s.pop(), s.pop()
            if orden == 'PRE':
                operando_izq, operando_der = operando_der, operando_izq

            s.append(Nodo_Expresion(c, operando_izq, operando_der))
        else:
            if (c[0] == '-' and c[1:].isnumeric()) or c.isnumeric():
                s.append(Nodo_Expresion(int(c)))

    if len(s) != 1:
        # si la pila no se consume completa la expresion no es correcta
        raise Exception("Expresion escrita incorrectamente.")
    
    # la ultima posicion en la pila tiene la raiz
    return s[-1]
    
def inorder(root: Nodo_Expresion) -> None:
    if type(root.val) == int:
        return str(root.val)
    
    if type(root.nodo_izq.val) == int and type(root.nodo_der.val) == int:
        return f"({inorder(root.nodo_izq)} {root.val} {inorder(root.nodo_der)})"
    
    return f"{inorder(root.nodo_izq)} {root.val} {inorder(root.nodo_der)}"

def eval(root: Nodo_Expresion) -> int:
    if root.nodo_izq is None and root.nodo_der is None:
        # estoy en una hoja
        return root.val

    if root.val == '+':
        return eval(root.nodo_izq) + eval(root.nodo_der)

    if root.val == '-':
        return eval(root.nodo_izq) - eval(root.nodo_der)
    
    if root.val == '*':
        return eval(root.nodo_izq) * eval(root.nodo_der)
    
    if eval(root.nodo_der) == 0:
        raise Exception("No esta permitida la division entre cero")
    return eval(root.nodo_izq) // eval(root.nodo_der)