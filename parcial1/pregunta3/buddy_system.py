from node import Node
from math import floor, log

class Buddy_System():
    def __init__(self, n):
        if (n <= 0):
            raise Exception("La cantidad de bloques debe ser mayor o igual que cero")
        self.total_blocks = 2**floor(log(n, 2))
        self.root = Node(self.total_blocks)
        self.empty_blocks = { self.total_blocks: 1}
        self.assigned_blocks = {}

    def reserve(self, name, size):
        # de ser posible, asignamos un bloque de tamano size al proceso name
        # retorna false si no se puede asignar el bloque
        if any(name in self.assigned_blocks[b] for b in self.assigned_blocks.keys()):
            return
        
        res = self.allocate(self.root, name, size)
        self.empty_blocks = {}
        self.assigned_blocks = {}
        self.update_list(self.root, self.empty_blocks, self.assigned_blocks)


    def free(self, name):
        # conseguimos un bloque y lo desasignamos
        if not any(name in self.assigned_blocks[b] for b in self.assigned_blocks.keys()):
            return
        
        # eliminamos desasignamos el bloque con nombre name
        self.unassigned_block(self.root, name)

        prev_e = {}
        prev_a = {}
        self.update_list(self.root, prev_e, prev_a)
        while (True):
            # en caso de que haya sucedido, fundimos dos bloques en uno
            self.join_blocks(self.root)

            curr_e = {}
            curr_a = {}
            self.update_list(self.root, curr_e, curr_a)
            
            # verificamos el punto fijo
            if curr_e == prev_e:
                break

            prev_e = curr_e
            prev_a = curr_a

        self.empty_blocks = curr_e
        self.assigned_blocks = curr_a

    def show(self):
        print(".: Bloque asignados:.")
        print("tamano bloques | procesos asignados | cantidad")
        for b in self.assigned_blocks.keys():
            print(f"{b} | {self.assigned_blocks[b]} | {len(self.assigned_blocks[b])}")


        print("\n.:Bloques vacios:.")
        print("tamano de bloque | cantidad de bloques libres")
        for b in self.empty_blocks:
            print(f"{b} | {self.empty_blocks[b]}")

    def allocate(self, node, name, size):
        # ubicamos el bloque que asignaremos
        if node.is_leaf() and node.name == "":
            # si el nodo es hoja lo revisamos
            # bloque libre sin dividir ni asignar
            if node.value//2 < size:
                node.name = name
                return True
            
            # si el bloque no se encuentra asignado, dividimos el bloque entre dos
            node.left = Node(node.value//2)
            node.right = Node(node.value//2)

            can_allocate = self.allocate(node.left, name, size)
            if not can_allocate:
                return self.allocate(node.right, name, size)
            
            return can_allocate
            
        elif node.is_leaf() and node.name != "":
            # bloque asignado
            return False
        
        else:
            # revisamos los subarboles
            if size <= node.value:
                can_allocate = self.allocate(node.left, name, size)
                if not can_allocate:
                    return self.allocate(node.right, name, size)
            
                return can_allocate
            
            return False
        
    def unassigned_block(self, node, name):
        if node.name == name:
            node.name = ""
        else:
            if not node.left is None:
                self.unassigned_block(node.left, name)
            
            if not node.right is None:
                self.unassigned_block(node.right, name)

    def join_blocks(self, node):
        if not node.is_leaf() and node.left.is_leaf()  and node.right.is_leaf():
            if node.left.name == "" and node.right.name == "":
                node.left = None
                node.right = None

        else:
            if not node.left is None:
                self.join_blocks(node.left)
            
            if not node.right is None:
                self.join_blocks(node.right)

    def update_list(self, node, empty, assigned):
        if node.is_leaf():
            if node.name == "":
                if not node.value in empty:
                    empty[node.value] = 0

                empty[node.value] += 1

            if node.name != "":
                if not node.value in assigned:
                    assigned[node.value] = []

                assigned[node.value].append(node.name)

        else:
            self.update_list(node.left, empty, assigned)
            self.update_list(node.right, empty, assigned) 