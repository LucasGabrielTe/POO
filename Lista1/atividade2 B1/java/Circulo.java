// Rascunho didático: complete os métodos marcados com TODO.
public class Circulo {
    private double raio;

    public Circulo(double raio) {
        this.raio = raio;
    }

    public double getRaio() { return raio; }
    public void setRaio(double raio) { this.raio = raio; }

    public double area() {
        throw new UnsupportedOperationException("TODO: calcular a área");
    }

    public double circunferencia() {
        throw new UnsupportedOperationException("TODO: calcular a circunferência");
    }
}