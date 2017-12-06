from math import sqrt


class Punto:
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        print(str(self.x) + "," + str(self.y))

    def cuadrante(self):
        if self.x >= 0 and self.y >= 0:
            print("Punto do primeiro cuadrante")
        elif self.x <= 0 and self.y >= 0:
            print("Punto do segundo cuadrante")
        elif self.x <= 0 and self.y <= 0:
            print("Punto do terceiro cuadrante")
        else:
            print("punto do cuarto cuadrante")

    def vector(self, punto):
        vx = punto.x - self.x
        vy = punto.y - self.y
        print("Vector: |{},{}|".format(vx, vy))

    def distancia(self, punto):
        distancia = sqrt((punto.x - self.x)**2 + (punto.y - self.y)**2)
        print("Distancia entre os dous puntos: {:.3f}".format(distancia))


class Rectangulo():
    def __init__(self, p1=Punto(), p2=Punto()):
        self.p1 = p1
        self.p2 = p2

    def base(self):
        self.base = abs(self.p1.x - self.p2.x)
        print("A base do rectángulo é {}".format(self.base))

    def altura(self):
        self.altura = abs(self.p1.y - self.p2.y)
        print("A altura do rectángulo é {}".format(self.altura))

    def area(self):
        self.base = abs(self.p1.x - self.p2.x)
        self.altura = abs(self.p1.y - self.p2.y)
        self.area = self.base * self.altura
        print("A area do rectangulo é {}".format(self.area))


A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto()

A.__str__()
B.__str__()
C.__str__()
D.__str__()

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)

r = Rectangulo(A, B)
r.base()
r.altura()
r.area()
