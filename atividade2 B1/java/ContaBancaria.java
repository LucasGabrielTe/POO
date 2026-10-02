// Rascunho didático: complete os métodos marcados com TODO.
public class ContaBancaria {
    private String titular;
    private String numero;
    private double saldo;

    public ContaBancaria(String titular, String numero, double saldo) {
        this.titular = titular;
        this.numero = numero;
        this.saldo = saldo;
    }

    public String getTitular() { return titular; }
    public String getNumero() { return numero; }
    public double getSaldo() { return saldo; }
    public void setSaldo(double saldo) { this.saldo = saldo; }

    public void depositar(double valor) {
        throw new UnsupportedOperationException("TODO: validar e depositar");
    }

    public boolean sacar(double valor) {
        throw new UnsupportedOperationException("TODO: validar e sacar");
    }
}