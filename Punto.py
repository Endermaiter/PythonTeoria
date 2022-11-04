import math
from math import pi


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print(super.__str__(self))
        return ' x = ' + str(self.x) + ' y = ' + str(self.y)


p = Punto(1, 2)

print(p)


class Circulo(Punto):
    """Crear un circulo nun punto dun plano cartesiano"""

    def __init__(self, x, y, r):
        Punto.__init__(self, x, y)
        self.r = r

    def area(self):
        return pi * (self.r ** 2)

    def perimetro(self):
        return 2 * pi * self.r

    def __str__(self):
        print(super.__str__(self))
        return 'x = ' + str(self.x) + ' y = ' + str(self.y) + ' r = ' + str(self.r)


class Prisma:

    def __init__(self, h):
        self.h = h


class Cilindro(Circulo, Prisma):

    def __init__(self, x=0, y=0, r=1, h=1):
        Circulo.__init__(self, x, y, r)
        Prisma.__init__(self, h)

    def area(self):
        return Circulo.area(self) * 2 + Circulo.perimetro(self) * self.h

    def volume(self):
        return Circulo.area(self) * self.h

    def __str__(self):
        return 'x = ' + str(self.x) + ' y = ' + str(self.y) + ' r = ' + str(self.r) + ' h = ' + str(self.h)


cilindro = Cilindro(4, 5, 2, 3)
print(cilindro.area())

cilindro.x = -7
print(cilindro)


from abc import ABC, abstractmethod

class Poligono(ABC):

    @abstractmethod
    def numeroDeLados(self):
        pass

class Triangulo(Poligono):

    def numeroDeLados(self):
        print("Numero de lados igual a 3")