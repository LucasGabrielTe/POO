from datetime import date

class Treino:
    def __init__(self, id, data_treino, distancia, tempo):
        self.__id = id
        self.__data = self._converter_data(data_treino)
        self.__distancia = 0.0
        self.__tempo = 0.0  # minutos
        self.SetDistancia(distancia)
        self.SetTempo(tempo)

    @staticmethod
    def _converter_data(valor):
        if isinstance(valor, date):
            return valor
        dia, mes, ano = map(int, valor.split("/"))
        return date(ano, mes, dia)

    def GetId(self): return self.__id
    def GetData(self): return self.__data
    def GetDistancia(self): return self.__distancia
    def GetTempo(self): return self.__tempo

    def SetId(self, valor): self.__id = valor
    def SetData(self, valor): self.__data = self._converter_data(valor)
    def SetDistancia(self, valor):
        valor = float(valor)
        if valor <= 0:
            raise ValueError("A distância deve ser maior que zero.")
        self.__distancia = valor

    def SetTempo(self, valor):
        valor = float(valor)
        if valor <= 0:
            raise ValueError("O tempo deve ser maior que zero.")
        self.__tempo = valor

    def Pace(self):
        if self.__distancia <= 0:
            raise ValueError("A distância deve ser maior que zero.")
        total_segundos = self.__tempo * 60
        segundos_km = total_segundos / self.__distancia
        minutos = int(segundos_km // 60)
        segundos = round(segundos_km % 60)
        if segundos == 60:
            minutos += 1
            segundos = 0
        return f"{minutos}:{segundos:02d} min/km"

    def velocidade_media(self):
        return self.__distancia / (self.__tempo / 60)

    def __str__(self):
        return (f"Treino {self.__id} | Data: {self.__data.strftime('%d/%m/%Y')} | "
                f"Distância: {self.__distancia:.2f} km | Tempo: {self.__tempo:.2f} min | "
                f"Pace: {self.Pace()}")


class TreinoUI:
    def __init__(self):
        self.__treinos = []

    def Inserir(self, treino):
        self.__treinos.append(treino)

    def Listar(self):
        return self.__treinos

    def Listar_Id(self, id):
        for treino in self.__treinos:
            if treino.GetId() == id:
                return treino
        return None

    def Atualizar(self, id, data=None, distancia=None, tempo=None):
        treino = self.Listar_Id(id)
        if treino is None:
            return False
        if data is not None: treino.SetData(data)
        if distancia is not None: treino.SetDistancia(distancia)
        if tempo is not None: treino.SetTempo(tempo)
        return True

    def Excluir(self, id):
        treino = self.Listar_Id(id)
        if treino is None:
            return False
        self.__treinos.remove(treino)
        return True

    def MaisRapido(self):
        if not self.__treinos:
            return None
        return min(self.__treinos, key=lambda t: t.GetTempo() / t.GetDistancia())

    def Menu(self):
        print("\n1 - Inserir")
        print("2 - Listar")
        print("3 - Listar por ID")
        print("4 - Atualizar")
        print("5 - Excluir")
        print("6 - Mais rápido")
        print("0 - Sair")

    def Main(self):
        while True:
            self.Menu()
            op = input("Opção: ")
            if op == "1":
                id = int(input("ID: "))
                data = input("Data (dd/mm/aaaa): ")
                distancia = float(input("Distância (km): "))
                tempo = float(input("Tempo (minutos): "))
                self.Inserir(Treino(id, data, distancia, tempo))
            elif op == "2":
                for t in self.Listar(): print(t)
            elif op == "3":
                t = self.Listar_Id(int(input("ID: ")))
                print(t if t else "Treino não encontrado.")
            elif op == "4":
                id = int(input("ID: "))
                data = input("Nova data (dd/mm/aaaa): ")
                distancia = float(input("Nova distância: "))
                tempo = float(input("Novo tempo (minutos): "))
                print("Atualizado." if self.Atualizar(id, data, distancia, tempo) else "Não encontrado.")
            elif op == "5":
                print("Excluído." if self.Excluir(int(input("ID: "))) else "Não encontrado.")
            elif op == "6":
                t = self.MaisRapido()
                print(t if t else "Nenhum treino cadastrado.")
            elif op == "0":
                break
            else:
                print("Opção inválida.")


if __name__ == "__main__":
    ui = TreinoUI()
    ui.Inserir(Treino(1, "01/10/2026", 5, 30))
    ui.Inserir(Treino(2, "02/10/2026", 5, 25))
    for t in ui.Listar(): print(t)
    print("Mais rápido:", ui.MaisRapido())
    # Para usar o menu, descomente:
    # ui.Main()
