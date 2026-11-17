// Rascunho didático: complete os métodos marcados com TODO.
public class Viagem {
    private double distancia;
    private double tempo;

    public Viagem(double distancia, double tempo) {
        this.distancia = distancia;
        this.tempo = tempo;
    }

    public double getDistancia() { return distancia; }
    public double getTempo() { return tempo; }
    public void setDistancia(double distancia) { this.distancia = distancia; }
    public void setTempo(double tempo) { this.tempo = tempo; }

    public double velocidadeMedia() {
        throw new UnsupportedOperationException("TODO: calcular velocidade média");
    }
}