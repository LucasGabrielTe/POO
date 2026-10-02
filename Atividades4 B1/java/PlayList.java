// Rascunho didático: complete os métodos marcados com TODO.
import java.util.ArrayList;
import java.util.List;

class Musica {
    private String titulo;
    private String artista;
    private String album;

    public Musica(String titulo, String artista, String album) {
        this.titulo = titulo;
        this.artista = artista;
        this.album = album;
    }
}

public class PlayList {
    private String nome;
    private String descricao;
    private final List<Musica> musicas = new ArrayList<>();

    public PlayList(String nome, String descricao) {
        this.nome = nome;
        this.descricao = descricao;
    }

    public void inserir(Musica musica) { musicas.add(musica); }
    public List<Musica> listar() { return musicas; }
}