from enum import Enum
from datetime import date

class SituacaoEstagio(Enum):
    Cadastrado = "Cadastrado"
    Iniciado = "Iniciado"
    Cancelado = "Cancelado"
    Finalizado = "Finalizado"


class Estagio:
    def __init__(self, nome_estagiario, nome_empresa):
        self.__nome_estagiario = nome_estagiario
        self.__nome_empresa = nome_empresa
        self.__data_inicio = None
        self.__data_cancelamento = None
        self.__data_fim = None
        self.__situacao = SituacaoEstagio.Cadastrado

    def GetEstagiario(self): return self.__nome_estagiario
    def GetEmpresa(self): return self.__nome_empresa
    def SetEstagiario(self, valor): self.__nome_estagiario = valor
    def SetEmpresa(self, valor): self.__nome_empresa = valor

    def Iniciar(self, data_inicio=None):
        if self.__situacao != SituacaoEstagio.Cadastrado:
            raise ValueError("O estágio não está cadastrado.")
        self.__data_inicio = data_inicio or date.today()
        self.__situacao = SituacaoEstagio.Iniciado

    def Cancelar(self, data_cancelamento=None):
        if self.__situacao != SituacaoEstagio.Iniciado:
            raise ValueError("Somente estágio iniciado pode ser cancelado.")
        self.__data_cancelamento = data_cancelamento or date.today()
        self.__situacao = SituacaoEstagio.Cancelado

    def Finalizar(self, data_fim=None):
        if self.__situacao != SituacaoEstagio.Iniciado:
            raise ValueError("Somente estágio iniciado pode ser finalizado.")
        self.__data_fim = data_fim or date.today()
        self.__situacao = SituacaoEstagio.Finalizado

    def GetDataInicio(self): return self.__data_inicio
    def GetDataCancelamento(self): return self.__data_cancelamento
    def GetDataFim(self): return self.__data_fim
    def GetSituacao(self): return self.__situacao

    def TempoEstagio(self):
        if self.__data_inicio is None:
            return "0 dias"
        fim = self.__data_cancelamento or self.__data_fim or date.today()
        dias = (fim - self.__data_inicio).days
        return f"{dias} dias"

    def ToString(self):
        return (f"Estagiário: {self.__nome_estagiario} | Empresa: {self.__nome_empresa} | "
                f"Início: {self.__data_inicio} | Cancelamento: {self.__data_cancelamento} | "
                f"Fim: {self.__data_fim} | Situação: {self.__situacao.value}")

    def __str__(self):
        return self.ToString()


class EstagioUI:
    def __init__(self):
        self.__estagios = []

    def Inserir(self, estagio):
        self.__estagios.append(estagio)

    def ListarPorEmpresa(self):
        return sorted(self.__estagios, key=lambda e: e.GetEmpresa().lower())

    def ListarPorEstagiario(self):
        return sorted(self.__estagios, key=lambda e: e.GetEstagiario().lower())

    def ListarPorSituacao(self, situacao):
        return [e for e in self.__estagios if e.GetSituacao() == situacao]


if __name__ == "__main__":
    e = Estagio("João", "Empresa X")
    e.Iniciar()
    print(e)
    print("Tempo:", e.TempoEstagio())
