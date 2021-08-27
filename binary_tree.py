
class Polygon:
    def __init__(self, regular):
        self.regular = regular

    def get_area(self):
        pass

    def get_perimetro(self):
        pass

    def print_shape(self):
        print("Area: ", self.get_area())
        print("Perimetro: ", self.get_perimetro())


class Retangulo(Polygon):
    def __init__(self, base, altura, regular):
        self.base = base
        self.altura = altura

    def get_area(self):
        return self.base * self.altura

    def get_perimetro(self):
        return (self.base * 2 + self.altura * 2)


class TrianguloI(Polygon):
    def __init__(self, altura, largura, base, regular):
        self.base = base
        self.altura = altura
        self.largura = largura

    def get_area(self):
        return (self.base * self.altura) / 2

    def get_perimetro(self):
        return (self.base + self.largura + self.largura)


class Circulo(Polygon):
    pi = 3.14
    def __init__(self, raio, regular):
        self.raio = raio

    def get_area(self):
        return (self.raio * self.raio) * Circulo.pi

    def get_perimetro(self):
        return 2 * 3.14 * self.raio


tri = TrianguloI(21, 8, 10, True)
ret = Retangulo(5, 4, True)
circ = Circulo(9, True)

polig = Polygon(True)
polig = tri
polig.print_shape()