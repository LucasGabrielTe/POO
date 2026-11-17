class Viagem:
    def __init__(self, distancia=0.0, tempo=0.0):
        self.__distancia = 0.0
        self.__tempo = 0.0
        self.set_distancia(distancia)
        self.set_tempo(tempo)

    def set_distancia(self, distancia):
        if distancia < 0:
            raise ValueError("A distância deve ser não negativa.")
        self.__distancia = float(distancia)

    def set_tempo(self, tempo):
        if tempo <= 0:
            raise ValueError("O tempo deve ser maior que zero.")
        self.__tempo = float(tempo)

    def get_distancia(self):
        return self.__distancia

    def get_tempo(self):
        return self.__tempo

    def velocidade_media(self):
        return self.__distancia / self.__tempo


if __name__ == "__main__":
    v = Viagem(210, 3.5)
    print("Distância:", v.get_distancia(), "km")
    print("Tempo:", v.get_tempo(), "h")
    print("Velocidade média:", v.velocidade_media(), "km/h")
