// Rascunho didático: complete os métodos marcados com TODO.
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

enum SituacaoEstagio { CADASTRADO, INICIADO, CANCELADO, FINALIZADO }

class EstagioItem {
    private String estagiario;
    private String empresa;
    private LocalDate dataInicio;
    private SituacaoEstagio situacao = SituacaoEstagio.CADASTRADO;

    public EstagioItem(String estagiario, String empresa) {
        this.estagiario = estagiario;
        this.empresa = empresa;
    }

    public void iniciar(LocalDate data) {
        throw new UnsupportedOperationException("TODO: iniciar o estágio");
    }
    public void cancelar(LocalDate data) {
        throw new UnsupportedOperationException("TODO: cancelar o estágio");
    }
    public void finalizar(LocalDate data) {
        throw new UnsupportedOperationException("TODO: finalizar o estágio");
    }
}

public class Estagio {
    private final List<EstagioItem> estagios = new ArrayList<>();
    public void inserir(EstagioItem estagio) { estagios.add(estagio); }
    public List<EstagioItem> listar() { return estagios; }
}