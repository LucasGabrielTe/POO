class Cliente:
    def __init__(self, nome, cpf, limite):
        self.__nome = nome
        self.__cpf = cpf
        self.__limite = float(limite)
        self.__socio = None

    def SetNome(self, nome): self.__nome = nome
    def SetCpf(self, cpf): self.__cpf = cpf
    def SetLimite(self, limite): self.__limite = float(limite)

    def GetNome(self): return self.__nome
    def GetCpf(self): return self.__cpf

    def SetSocio(self, socio):
        if socio is self:
            raise ValueError("Um cliente não pode ser sócio de si mesmo.")
        self.__socio = socio
        if socio is not None and socio.__socio is not self:
            socio.__socio = self

    def GetLimite(self):
        if self.__socio is None:
            return self.__limite
        return self.__limite + self.__socio.__limite

    def ToString(self):
        socio = self.__socio.__nome if self.__socio else "Nenhum"
        return f"Cliente: {self.__nome} | CPF: {self.__cpf} | Limite próprio: R$ {self.__limite:.2f} | Sócio: {socio} | Limite total: R$ {self.GetLimite():.2f}"

    def __str__(self):
        return self.ToString()


class Empresa:
    def __init__(self, nome):
        self.__nome = nome
        self.__clientes = []

    def SetNome(self, nome): self.__nome = nome
    def GetNome(self): return self.__nome

    def Inserir(self, cliente):
        self.__clientes.append(cliente)

    def Listar(self):
        return self.__clientes


if __name__ == "__main__":
    empresa = Empresa("Cartões ABC")
    c1 = Cliente("Ana", "111", 1000)
    c2 = Cliente("Bruno", "222", 1500)
    c1.SetSocio(c2)
    empresa.Inserir(c1)
    empresa.Inserir(c2)
    print(empresa.GetNome())
    for c in empresa.Listar():
        print(c)
