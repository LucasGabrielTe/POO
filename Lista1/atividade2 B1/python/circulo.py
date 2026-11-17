import math

class Circulo:
    def __init__(self, raio=0.0):
        self.__raio = 0.0
        self.set_raio(raio)

    def set_raio(self, raio):
        if raio < 0:
            raise ValueError("O raio deve ser não negativo.")
        self.__raio = float(raio)

    def get_raio(self):
        return self.__raio

    def area(self):
        return math.pi * self.__raio ** 2

    def circunferencia(self):
        return 2 * math.pi * self.__raio


if __name__ == "__main__":
    c = Circulo(5)
    print("Raio:", c.get_raio())
    print("Área:", c.area())
    print("Circunferência:", c.circunferencia())
