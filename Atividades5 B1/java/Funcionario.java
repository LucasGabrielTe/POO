// Rascunho didático: complete os métodos marcados com TODO.
enum Turno { MANHA, TARDE, NOITE, INTEGRAL }
enum Cargo { ESTAGIARIO, JUNIOR, PLENO, SENIOR, GERENTE }

public class Funcionario {
    private String nome;
    private String matricula;
    private double salario;
    private Cargo cargo;
    private Turno turno;

    public Funcionario(String nome, String matricula, double salario, Cargo cargo, Turno turno) {
        this.nome = nome;
        this.matricula = matricula;
        this.salario = salario;
        this.cargo = cargo;
        this.turno = turno;
    }

    public void promover() {
        throw new UnsupportedOperationException("TODO: atualizar cargo e salário");
    }
    public String tempoTrabalho() {
        throw new UnsupportedOperationException("TODO: calcular tempo de trabalho");
    }
}