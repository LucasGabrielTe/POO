import math

class Retangulo:
    def __init__(self, b, h):
        self.__b = 0.0
        self.__h = 0.0
        self.SetBase(b)
        self.SetAltura(h)

    def SetBase(self, b):
        if b <= 0:
            raise ValueError("A base deve ser positiva.")
        self.__b = float(b)

    def SetAltura(self, h):
        if h <= 0:
            raise ValueError("A altura deve ser positiva.")
        self.__h = float(h)

    def GetBase(self):
        return self.__b

    def GetAltura(self):
        return self.__h

    def CalcArea(self):
        return self.__b * self.__h

    def CalcDiagonal(self):
        return math.sqrt(self.__b ** 2 + self.__h ** 2)

    def ToString(self):
        return f"Retângulo: base={self.__b}, altura={self.__h}"

    def __str__(self):
        return self.ToString()


if __name__ == "__main__":
    r = Retangulo(3, 4)
    print(r)
    print("Área:", r.CalcArea())
    print("Diagonal:", r.CalcDiagonal())
