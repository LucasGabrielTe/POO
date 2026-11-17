// Rascunho didático: complete os métodos marcados com TODO.
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

class Playlist {
    int id;
    String nome;
    String descricao;
    Playlist(int id, String nome, String descricao) {
        this.id = id; this.nome = nome; this.descricao = descricao;
    }
}

class MusicaItem {
    int id;
    String titulo;
    String artista;
    String album;
    int duracaoSegundos;
    MusicaItem(int id, String titulo, String artista, String album, int duracaoSegundos) {
        this.id = id; this.titulo = titulo; this.artista = artista;
        this.album = album; this.duracaoSegundos = duracaoSegundos;
    }
}

class PlaylistItem {
    int id;
    int idPlaylist;
    int idMusica;
    LocalDate dataInclusao;
    int sequencia;
}

public class PlaylistApp {
    private final List<Playlist> playlists = new ArrayList<>();
    private final List<MusicaItem> musicas = new ArrayList<>();
    private final List<PlaylistItem> itens = new ArrayList<>();

    public List<MusicaItem> listarMusicasDaPlaylist(int idPlaylist) {
        throw new UnsupportedOperationException("TODO: relacionar e ordenar músicas");
    }
    public boolean excluirPlaylist(int id) {
        throw new UnsupportedOperationException("TODO: excluir playlist e seus itens");
    }
}