class PlayList:
    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao
        self.__musicas = []

    def set_nome(self, nome):
        self.__nome = nome

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao

    def inserir(self, musica):
        self.__musicas.append(musica)

    def listar(self):
        return self.__musicas

    def to_string(self):
        return f"Playlist: {self.__nome} | Descrição: {self.__descricao} | Músicas: {len(self.__musicas)}"

    def __str__(self):
        return self.to_string()

    # Compatibilidade com o estilo antigo
    def SetNome(self, nome): self.set_nome(nome)
    def SetDescricao(self, descricao): self.set_descricao(descricao)
    def GetNome(self): return self.get_nome()
    def GetDescricao(self): return self.get_descricao()
    def Inserir(self, musica): self.inserir(musica)
    def Listar(self): return self.listar()
    def ToString(self): return self.to_string()


class Musica:
    def __init__(self, titulo, artista, album):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_artista(self, artista):
        self.__artista = artista

    def set_album(self, album):
        self.__album = album

    def get_titulo(self):
        return self.__titulo

    def get_artista(self):
        return self.__artista

    def get_album(self):
        return self.__album

    def to_string(self):
        return f"Título: {self.__titulo} | Artista: {self.__artista} | Álbum: {self.__album}"

    def __str__(self):
        return self.to_string()

    # Compatibilidade com o estilo antigo
    def SetTitulo(self, titulo): self.set_titulo(titulo)
    def SetArtista(self, artista): self.set_artista(artista)
    def SetAlbum(self, album): self.set_album(album)
    def GetTitulo(self): return self.get_titulo()
    def GetArtista(self): return self.get_artista()
    def GetAlbum(self): return self.get_album()
    def ToString(self): return self.to_string()


if __name__ == "__main__":
    p = PlayList("Rock", "Músicas de rock")
    p.inserir(Musica("My Demons", "Starset", "Transmissions"))
    p.inserir(Musica("Everlong", "Foo Fighters", "The Colour and the Shape"))
    print(p)
    for musica in p.listar():
        print(musica)
