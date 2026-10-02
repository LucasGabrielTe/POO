class Frete:
    def __init__(self, distancia, peso):
        self.__distancia = 0.0
        self.__peso = 0.0
        self.SetDistancia(distancia)
        self.SetPeso(peso)

    def SetDistancia(self, distancia):
        if distancia <= 0:
            raise ValueError("A distância deve ser positiva.")
        self.__distancia = float(distancia)

    def SetPeso(self, peso):
        if peso <= 0:
            raise ValueError("O peso deve ser positivo.")
        self.__peso = float(peso)

    def GetDistancia(self):
        return self.__distancia

    def GetPeso(self):
        return self.__peso

    def CalcFrete(self):
        return self.__distancia * self.__peso * 0.01

    def ToString(self):
        return f"Frete: distância={self.__distancia} km, peso={self.__peso} kg"

    def __str__(self):
        return self.ToString()


if __name__ == "__main__":
    f = Frete(100, 20)
    print(f)
    print("Valor do frete: R$", f.CalcFrete())
