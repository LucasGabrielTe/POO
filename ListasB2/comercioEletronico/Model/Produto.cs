namespace comercioEletronico.Model
{
    public class Produto
    {
        public int Id { get; set; }
        public string Descricao { get; set; }
        public double Preco { get; set; }
        public int Estoque { get; set; }
        public int IdCategoria { get; set; }

        public Produto(string descricao, double preco, int estoque, int idcategoria)
        {
            Descricao = descricao;
            Preco = preco;
            Estoque = estoque;
            IdCategoria = idcategoria;
        }
    }
}
