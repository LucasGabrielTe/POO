// Rascunho didático: complete os métodos marcados com TODO.
public class Frete {
    private double distancia;
    private double peso;

    public Frete(double distancia, double peso) {
        this.distancia = distancia;
        this.peso = peso;
    }

    public double calcularFrete() {
        throw new UnsupportedOperationException("TODO: calcular o valor do frete");
    }

    @Override
    public String toString() {
        throw new UnsupportedOperationException("TODO: formatar os dados do frete");
    }
}