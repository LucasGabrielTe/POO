// Rascunho didático: complete os métodos marcados com TODO.
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

class PacienteItem {
    private String nome;
    private String cpf;
    private String telefone;
    private LocalDate nascimento;

    public PacienteItem(String nome, String cpf, String telefone, LocalDate nascimento) {
        this.nome = nome;
        this.cpf = cpf;
        this.telefone = telefone;
        this.nascimento = nascimento;
    }

    public String idade() {
        throw new UnsupportedOperationException("TODO: calcular idade");
    }
}

public class Paciente {
    private final List<PacienteItem> pacientes = new ArrayList<>();
    public void inserir(PacienteItem paciente) { pacientes.add(paciente); }
    public List<PacienteItem> listarPorNome() {
        throw new UnsupportedOperationException("TODO: ordenar pacientes por nome");
    }
    public List<PacienteItem> listarPorIdade() {
        throw new UnsupportedOperationException("TODO: ordenar pacientes por idade");
    }
}