class Node():
    def __init__(self, val):
        self.value = val
        self.name = ""
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None