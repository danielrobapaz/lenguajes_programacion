import numpy as np
from random import randint
from Vectores import Vector
from time import time


a, b = 1, 100
n = 100000000
elem1 = [randint(a, b)] * n
elem2 = [randint(a, b)] * n

vector1 = Vector(elem1)
vector2 = Vector(elem2)

start = time()
res = vector1.producto_punto(vector2)
print(f"con hilos: {time() - start} segundos")


start = time()
res = np.dot(elem1, elem2)
print(f"sin hilos: {time() - start} segundos")