// Rascunho didático: complete os métodos marcados com TODO.
public class Data {
    private int dia;
    private int mes;
    private int ano;

    public Data(int dia, int mes, int ano) {
        this.dia = dia;
        this.mes = mes;
        this.ano = ano;
    }

    public int getDia() { return dia; }
    public int getMes() { return mes; }
    public int getAno() { return ano; }
    public void setData(String texto) {
        throw new UnsupportedOperationException("TODO: validar e ler dd/mm/aaaa");
    }

    @Override
    public String toString() {
        throw new UnsupportedOperationException("TODO: formatar a data");
    }
}