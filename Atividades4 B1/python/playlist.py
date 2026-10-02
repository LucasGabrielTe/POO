class PlayList:
    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao
        self.__musicas = []

    def SetNome(self, nome): self.__nome = nome
    def SetDescricao(self, descricao): self.__descricao = descricao
    def GetNome(self): return self.__nome
    def GetDescricao(self): return self.__descricao

    def Inserir(self, musica):
        self.__musicas.append(musica)

    def Listar(self):
        return self.__musicas

    def ToString(self):
        return f"Playlist: {self.__nome} | Descrição: {self.__descricao} | Músicas: {len(self.__musicas)}"

    def __str__(self):
        return self.ToString()


class Musica:
    def __init__(self, titulo, artista, album):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album

    def SetTitulo(self, titulo): self.__titulo = titulo
    def SetArtista(self, artista): self.__artista = artista
    def SetAlbum(self, album): self.__album = album
    def GetTitulo(self): return self.__titulo
    def GetArtista(self): return self.__artista
    def GetAlbum(self): return self.__album

    def ToString(self):
        return f"Título: {self.__titulo} | Artista: {self.__artista} | Álbum: {self.__album}"

    def __str__(self):
        return self.ToString()


if __name__ == "__main__":
    p = PlayList("Rock", "Músicas de rock")
    p.Inserir(Musica("My Demons", "Starset", "Transmissions"))
    p.Inserir(Musica("Everlong", "Foo Fighters", "The Colour and the Shape"))
    print(p)
    for m in p.Listar():
        print(m)
