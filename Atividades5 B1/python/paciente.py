from datetime import date

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = self._converter_data(nascimento)

    @staticmethod
    def _converter_data(valor):
        if isinstance(valor, date):
            return valor
        dia, mes, ano = map(int, valor.split("/"))
        return date(ano, mes, dia)

    def GetNome(self): return self.__nome
    def GetCpf(self): return self.__cpf
    def GetTelefone(self): return self.__telefone
    def GetDataNascimento(self): return self.__nascimento

    def SetNome(self, valor): self.__nome = valor
    def SetCpf(self, valor): self.__cpf = valor
    def SetTelefone(self, valor): self.__telefone = valor
    def SetDataNascimento(self, valor): self.__nascimento = self._converter_data(valor)

    def Idade(self):
        hoje = date.today()
        anos = hoje.year - self.__nascimento.year
        meses = hoje.month - self.__nascimento.month
        if hoje.day < self.__nascimento.day:
            meses -= 1
        if meses < 0:
            anos -= 1
            meses += 12
        return f"{anos} anos e {meses} meses"

    def ToString(self):
        nasc = self.__nascimento.strftime("%d/%m/%Y")
        return f"Paciente: {self.__nome} | CPF: {self.__cpf} | Telefone: {self.__telefone} | Nascimento: {nasc}"

    def __str__(self):
        return self.ToString()


class PacienteUI:
    def __init__(self):
        self.__pacientes = []

    def Inserir(self, paciente):
        self.__pacientes.append(paciente)

    def ListarNome(self):
        return sorted(self.__pacientes, key=lambda p: p.GetNome().lower())

    def ListarIdade(self):
        return sorted(self.__pacientes, key=lambda p: p.GetDataNascimento())


if __name__ == "__main__":
    ui = PacienteUI()
    ui.Inserir(Paciente("Carlos", "111", "9999", "10/05/2000"))
    ui.Inserir(Paciente("Ana", "222", "8888", "20/03/1998"))
    print("Por nome:")
    for p in ui.ListarNome(): print(p)
    print("Por idade:")
    for p in ui.ListarIdade(): print(p, "-", p.Idade())
