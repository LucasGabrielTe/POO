// Rascunho didático: complete os métodos marcados com TODO.
import java.util.ArrayList;
import java.util.List;

class Cliente {
    private String nome;
    private String cpf;
    private double limite;
    private Cliente socio;

    public Cliente(String nome, String cpf, double limite) {
        this.nome = nome;
        this.cpf = cpf;
        this.limite = limite;
    }

    public void setSocio(Cliente socio) {
        throw new UnsupportedOperationException("TODO: validar e associar sócio");
    }
    public double getLimiteTotal() {
        throw new UnsupportedOperationException("TODO: calcular limite total");
    }
}

public class Empresa {
    private String nome;
    private final List<Cliente> clientes = new ArrayList<>();

    public Empresa(String nome) { this.nome = nome; }
    public void inserir(Cliente cliente) { clientes.add(cliente); }
    public List<Cliente> listar() { return clientes; }
}