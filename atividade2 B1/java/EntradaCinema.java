// Rascunho didático: complete os métodos marcados com TODO.
public class EntradaCinema {
    private String dia;
    private int horario;

    public EntradaCinema(String dia, int horario) {
        this.dia = dia;
        this.horario = horario;
    }

    public void setHorario(int horario) { this.horario = horario; }
    public double valorInteira() {
        throw new UnsupportedOperationException("TODO: calcular preço da inteira");
    }
    public double valorMeia() {
        throw new UnsupportedOperationException("TODO: calcular preço da meia");
    }
}