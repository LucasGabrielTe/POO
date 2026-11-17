from datetime import date

class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = 0
        self.__mes = 0
        self.__ano = 0
        self._set_data_valida(dia, mes, ano)

    @staticmethod
    def _validar(dia, mes, ano):
        try:
            date(ano, mes, dia)
            return True
        except (ValueError, TypeError):
            return False

    def _set_data_valida(self, dia, mes, ano):
        if not self._validar(dia, mes, ano):
            raise ValueError("Data inválida.")
        self.__dia = int(dia)
        self.__mes = int(mes)
        self.__ano = int(ano)

    def GetDia(self): return self.__dia
    def GetMes(self): return self.__mes
    def GetAno(self): return self.__ano

    def SetData(self, texto):
        try:
            dia, mes, ano = map(int, texto.split("/"))
        except ValueError:
            raise ValueError("Use o formato dd/mm/aaaa.")
        self._set_data_valida(dia, mes, ano)

    def ToString(self):
        return f"{self.__dia:02d}/{self.__mes:02d}/{self.__ano:04d}"

    def __str__(self):
        return self.ToString()


if __name__ == "__main__":
    d = Data(2, 10, 2026)
    print(d)
    d.SetData("15/12/2026")
    print(d)
