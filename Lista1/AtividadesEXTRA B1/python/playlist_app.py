from datetime import date

class PlayList:
    def __init__(self, id, nome, descricao):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao

    def GetId(self): return self.__id
    def GetNome(self): return self.__nome
    def GetDescricao(self): return self.__descricao
    def SetId(self, v): self.__id = v
    def SetNome(self, v): self.__nome = v
    def SetDescricao(self, v): self.__descricao = v

    def ToString(self):
        return f"Playlist {self.__id}: {self.__nome} | {self.__descricao}"

    def __str__(self):
        return self.ToString()


class Musica:
    def __init__(self, id, titulo, artista, album, duracao):
        self.__id = id
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
        self.__duracao = int(duracao)  # segundos

    def GetId(self): return self.__id
    def GetTitulo(self): return self.__titulo
    def GetArtista(self): return self.__artista
    def GetAlbum(self): return self.__album
    def GetDuracao(self): return self.__duracao
    def SetId(self, v): self.__id = v
    def SetTitulo(self, v): self.__titulo = v
    def SetArtista(self, v): self.__artista = v
    def SetAlbum(self, v): self.__album = v
    def SetDuracao(self, v): self.__duracao = int(v)

    def __str__(self):
        m, s = divmod(self.__duracao, 60)
        return f"Música {self.__id}: {self.__titulo} - {self.__artista} | {self.__album} | {m}:{s:02d}"


class PlayListItem:
    def __init__(self, id, id_playlist, id_musica, data_inclusao, sequencia):
        self.__id = id
        self.__id_playlist = id_playlist
        self.__id_musica = id_musica
        self.__data_inclusao = self._converter_data(data_inclusao)
        self.__sequencia = int(sequencia)

    @staticmethod
    def _converter_data(v):
        if isinstance(v, date): return v
        d, m, a = map(int, v.split("/"))
        return date(a, m, d)

    def GetId(self): return self.__id
    def GetIdPlaylist(self): return self.__id_playlist
    def GetIdMusica(self): return self.__id_musica
    def GetDataInclusao(self): return self.__data_inclusao
    def GetSequencia(self): return self.__sequencia
    def SetId(self, v): self.__id = v
    def SetIdPlaylist(self, v): self.__id_playlist = v
    def SetIdMusica(self, v): self.__id_musica = v
    def SetDataInclusao(self, v): self.__data_inclusao = self._converter_data(v)
    def SetSequencia(self, v): self.__sequencia = int(v)

    def __str__(self):
        return (f"Item {self.__id}: playlist={self.__id_playlist}, música={self.__id_musica}, "
                f"data={self.__data_inclusao.strftime('%d/%m/%Y')}, sequência={self.__sequencia}")


class UI:
    def __init__(self):
        self.playlists = []
        self.musicas = []
        self.itens = []

    def InserirPlaylist(self, p): self.playlists.append(p)
    def InserirMusica(self, m): self.musicas.append(m)
    def InserirItem(self, item): self.itens.append(item)

    def ListarPlaylists(self): return self.playlists
    def ListarMusicas(self): return self.musicas
    def ListarItens(self): return self.itens

    def Playlist(self, id):
        return next((p for p in self.playlists if p.GetId() == id), None)

    def Musica(self, id):
        return next((m for m in self.musicas if m.GetId() == id), None)

    def ItensPlaylist(self, id_playlist):
        return sorted([i for i in self.itens if i.GetIdPlaylist() == id_playlist],
                      key=lambda i: i.GetSequencia())

    def ListarMusicasDaPlaylist(self, id_playlist):
        resultado = []
        for item in self.ItensPlaylist(id_playlist):
            musica = self.Musica(item.GetIdMusica())
            if musica:
                resultado.append(musica)
        return resultado

    def AtualizarPlaylist(self, id, nome=None, descricao=None):
        p = self.Playlist(id)
        if not p: return False
        if nome is not None: p.SetNome(nome)
        if descricao is not None: p.SetDescricao(descricao)
        return True

    def ExcluirPlaylist(self, id):
        p = self.Playlist(id)
        if not p: return False
        self.playlists.remove(p)
        self.itens = [i for i in self.itens if i.GetIdPlaylist() != id]
        return True

    def AtualizarMusica(self, id, titulo=None, artista=None, album=None, duracao=None):
        m = self.Musica(id)
        if not m: return False
        if titulo is not None: m.SetTitulo(titulo)
        if artista is not None: m.SetArtista(artista)
        if album is not None: m.SetAlbum(album)
        if duracao is not None: m.SetDuracao(duracao)
        return True

    def ExcluirMusica(self, id):
        m = self.Musica(id)
        if not m: return False
        self.musicas.remove(m)
        self.itens = [i for i in self.itens if i.GetIdMusica() != id]
        return True

    def AtualizarItem(self, id, id_playlist=None, id_musica=None, data=None, sequencia=None):
        item = next((i for i in self.itens if i.GetId() == id), None)
        if not item: return False
        if id_playlist is not None: item.SetIdPlaylist(id_playlist)
        if id_musica is not None: item.SetIdMusica(id_musica)
        if data is not None: item.SetDataInclusao(data)
        if sequencia is not None: item.SetSequencia(sequencia)
        return True

    def ExcluirItem(self, id):
        item = next((i for i in self.itens if i.GetId() == id), None)
        if not item: return False
        self.itens.remove(item)
        return True

    def Main(self):
        while True:
            print("\n1-Listar playlists  2-Listar músicas  3-Listar itens  4-Músicas da playlist  0-Sair")
            op = input("Opção: ")
            if op == "1":
                for x in self.playlists: print(x)
            elif op == "2":
                for x in self.musicas: print(x)
            elif op == "3":
                for x in self.itens: print(x)
            elif op == "4":
                pid = int(input("ID da playlist: "))
                for x in self.ListarMusicasDaPlaylist(pid): print(x)
            elif op == "0":
                break


if __name__ == "__main__":
    ui = UI()
    ui.InserirPlaylist(PlayList(1, "Rock", "Rock internacional"))
    ui.InserirMusica(Musica(1, "My Demons", "Starset", "Transmissions", 265))
    ui.InserirItem(PlayListItem(1, 1, 1, "02/10/2026", 1))
    print(ui.playlists[0])
    print(ui.musicas[0])
    print("Músicas da playlist:", ui.ListarMusicasDaPlaylist(1))
