import math

class EquacaoSegundoGrau:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def SetA(self, a): self.__a = a
    def SetB(self, b): self.__b = b
    def SetC(self, c): self.__c = c
    def GetA(self): return self.__a
    def GetB(self): return self.__b
    def GetC(self): return self.__c

    def Delta(self):
        return self.__b ** 2 - 4 * self.__a * self.__c

    def TemRaizesReais(self):
        return self.__a != 0 and self.Delta() >= 0

    def Raiz1(self):
        if not self.TemRaizesReais():
            return None
        return (-self.__b + math.sqrt(self.Delta())) / (2 * self.__a)

    def Raiz2(self):
        if not self.TemRaizesReais():
            return None
        return (-self.__b - math.sqrt(self.Delta())) / (2 * self.__a)

    def ToString(self):
        return f"Equação: a={self.__a}, b={self.__b}, c={self.__c}"

    def __str__(self):
        return self.ToString()


if __name__ == "__main__":
    e = EquacaoSegundoGrau(1, -5, 6)
    print(e)
    print("Delta:", e.Delta())
    print("Tem raízes reais?", e.TemRaizesReais())
    print("Raiz 1:", e.Raiz1())
    print("Raiz 2:", e.Raiz2())
