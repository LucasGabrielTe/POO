// Rascunho didático: complete os métodos marcados com TODO.
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

class TreinoItem {
    private int id;
    private LocalDate data;
    private double distancia;
    private double tempoMinutos;

    public TreinoItem(int id, LocalDate data, double distancia, double tempoMinutos) {
        this.id = id;
        this.data = data;
        this.distancia = distancia;
        this.tempoMinutos = tempoMinutos;
    }

    public String pace() {
        throw new UnsupportedOperationException("TODO: calcular pace em min/km");
    }
}

public class Treino {
    private final List<TreinoItem> treinos = new ArrayList<>();
    public void inserir(TreinoItem treino) { treinos.add(treino); }
    public TreinoItem maisRapido() {
        throw new UnsupportedOperationException("TODO: encontrar o treino mais rápido");
    }
}