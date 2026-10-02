class Conversor:
    def __init__(self, num):
        self.__num = 0
        self.SetNum(num)

    def SetNum(self, num):
        num = int(num)
        if num < 0:
            raise ValueError("O número deve ser inteiro e positivo.")
        self.__num = num

    def GetNum(self):
        return self.__num

    def Binario(self):
        return bin(self.__num)[2:]

    def ToString(self):
        return f"Decimal: {self.__num} | Binário: {self.Binario()}"

    def __str__(self):
        return self.ToString()


if __name__ == "__main__":
    c = Conversor(25)
    print(c)
