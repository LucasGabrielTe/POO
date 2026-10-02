from enum import Enum
from datetime import date

class Turno(Enum):
    MANHA = "Manhã"
    TARDE = "Tarde"
    NOITE = "Noite"
    INTEGRAL = "Integral"


class Cargo(Enum):
    ESTAGIARIO = "Estagiário"
    JUNIOR = "Júnior"
    PLENO = "Pleno"
    SENIOR = "Sênior"
    GERENTE = "Gerente"


class Funcionario:
    def __init__(self, nome, matricula, salario, cargo, turno, data_admissao):
        self.__nome = nome
        self.__matricula = matricula
        self.__salario = float(salario)
        self.__cargo = cargo
        self.__turno = turno
        self.__data_admissao = self._converter_data(data_admissao)

    @staticmethod
    def _converter_data(valor):
        if isinstance(valor, date):
            return valor
        dia, mes, ano = map(int, valor.split("/"))
        return date(ano, mes, dia)

    def GetNome(self): return self.__nome
    def GetMatricula(self): return self.__matricula
    def GetSalario(self): return self.__salario
    def GetCargo(self): return self.__cargo
    def GetTurno(self): return self.__turno
    def GetDataAdmissao(self): return self.__data_admissao

    def SetNome(self, valor): self.__nome = valor
    def SetMatricula(self, valor): self.__matricula = valor
    def SetSalario(self, valor): self.__salario = float(valor)
    def SetCargo(self, valor): self.__cargo = valor
    def SetTurno(self, valor): self.__turno = valor
    def SetDataAdmissao(self, valor): self.__data_admissao = self._converter_data(valor)

    def TempoTrabalho(self):
        hoje = date.today()
        anos = hoje.year - self.__data_admissao.year
        meses = hoje.month - self.__data_admissao.month
        if hoje.day < self.__data_admissao.day:
            meses -= 1
        if meses < 0:
            anos -= 1
            meses += 12
        return f"{anos} anos e {meses} meses"

    def Promover(self):
        cargos = list(Cargo)
        pos = cargos.index(self.__cargo)
        if pos < len(cargos) - 1:
            self.__cargo = cargos[pos + 1]
            self.__salario *= 1.25

    def ToString(self):
        data = self.__data_admissao.strftime("%d/%m/%Y")
        return (f"Funcionário: {self.__nome} | Matrícula: {self.__matricula} | "
                f"Salário: R$ {self.__salario:.2f} | Cargo: {self.__cargo.value} | "
                f"Turno: {self.__turno.value} | Admissão: {data}")

    def __str__(self):
        return self.ToString()


if __name__ == "__main__":
    f = Funcionario("Maria", "001", 2000, Cargo.JUNIOR, Turno.MANHA, "10/01/2024")
    print(f)
    print("Tempo de trabalho:", f.TempoTrabalho())
    f.Promover()
    print("Após promoção:", f)
