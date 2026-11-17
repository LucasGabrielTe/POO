using System.Collections.Generic;
using System.Linq;
using comercioEletronico.Model;

namespace comercioEletronico.DAO
{
    public class ProdutoDAO
    {
        private List<Produto> produtos = new List<Produto>();
        private int proximoId = 1;

        public void Inserir(Produto produto)
        {
            produto.Id = proximoId;
            proximoId++;
            produtos.Add(produto);
        }

        public List<Produto> Listar()
        {
            return produtos;
        }

        public Produto? Listar_Id(int id)
        {
            return produtos.FirstOrDefault(p => p.Id == id);
        }

        public bool Atualizar(Produto produto)
        {
            Produto? existente = Listar_Id(produto.Id);

            if (existente == null)
                return false;

            existente.Descricao = produto.Descricao;
            existente.Preco = produto.Preco;
            existente.Estoque = produto.Estoque;
            existente.IdCategoria = produto.IdCategoria;

            return true;
        }

        public bool Excluir(int id)
        {
            Produto? produto = Listar_Id(id);

            if (produto == null)
                return false;

            produtos.Remove(produto);
            return true;
        }
    }
}