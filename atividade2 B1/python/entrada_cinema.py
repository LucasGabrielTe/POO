class EntradaCinema:
    def __init__(self, dia="", horario=0):
        self.__dia = dia
        self.__horario = 0
        self.set_horario(horario)

    def set_dia(self, dia):
        self.__dia = dia

    def get_dia(self):
        return self.__dia

    def set_horario(self, horario):
        if not 0 <= int(horario) <= 23:
            raise ValueError("Horário deve estar entre 0 e 23.")
        self.__horario = int(horario)

    def get_horario(self):
        return self.__horario

    def _valor_base(self):
        dia = self.__dia.strip().lower()
        if dia in ("quarta", "quarta-feira", "quarta feira"):
            return 8.00
        if dia in ("segunda", "terça", "terca", "quinta"):
            return 16.00
        if dia in ("sexta", "sábado", "sabado", "domingo"):
            return 20.00
        raise ValueError("Dia da semana inválido.")

    def valor_inteira(self):
        if self.__dia.strip().lower() in ("quarta", "quarta-feira", "quarta feira"):
            return 8.00
        valor = self._valor_base()
        if self.__horario >= 17:
            valor *= 1.5
        return valor

    def valor_meia(self):
        if self.__dia.strip().lower() in ("quarta", "quarta-feira", "quarta feira"):
            return 8.00
        return self.valor_inteira() / 2


if __name__ == "__main__":
    ingresso = EntradaCinema("sábado", 18)
    print("Inteira: R$", ingresso.valor_inteira())
    print("Meia: R$", ingresso.valor_meia())
