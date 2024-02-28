#!/usr/bin/env python3

class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

class Color:
    def __init__(self, color):
        self.color = color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, alto=lado, ancho=lado)
        Color.__init__(self, color=color)

    def area(self):
        return self.ancho * self.alto

    def __str__(self):
        return f'Cuadrado [lado={self.alto}, color={self.color}]'

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto=alto, ancho=ancho)
        Color.__init__(self, color=color)

    def area(self):
        return self.ancho * self.alto

    def __str__(self):
        return f'Rectangulo [alto={self.alto}, ancho={self.ancho}, color={self.color}]'

if __name__ == "__main__":
    c1 = Cuadrado(lado=9, color="Rojo")
    print(c1)

    r1 = Rectangulo(alto=5, ancho=10, color="Azul")
    print(r1)
    print(c1.area())
