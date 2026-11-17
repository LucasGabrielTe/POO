// Rascunho didático: complete os métodos marcados com TODO.
public class Conversor {
    private int numero;

    public Conversor(int numero) { this.numero = numero; }
    public int getNumero() { return numero; }
    public void setNumero(int numero) { this.numero = numero; }

    public String binario() {
        throw new UnsupportedOperationException("TODO: converter para binário");
    }

    @Override
    public String toString() {
        throw new UnsupportedOperationException("TODO: formatar os valores");
    }
}