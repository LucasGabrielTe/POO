using System.Collections.Generic;
using comercioEletronico.Model;
using comercioEletronico.DAO;

namespace comercioEletronico.Service
{
    public class Service
    {
        private ClienteDAO clienteDAO = new ClienteDAO();
        private CategoriaDAO categoriaDAO = new CategoriaDAO();
        private ProdutoDAO produtoDAO = new ProdutoDAO();

        public void InserirCliente(string nome, string email, string fone)
        {
            Cliente cliente = new Cliente(nome, email, fone);
            clienteDAO.Inserir(cliente);
        }

        public List<Cliente> ListarClientes()
        {
            return clienteDAO.Listar();
        }

        public Cliente? ListarClientePorId(int id)
        {
            return clienteDAO.Listar_Id(id);
        }

        public bool AtualizarCliente(int id, string nome, string email, string fone)
        {
            Cliente cliente = new Cliente(nome, email, fone);
            cliente.Id = id;

            return clienteDAO.Atualizar(cliente);
        }

        public bool ExcluirCliente(int id)
        {
            return clienteDAO.Excluir(id);
        }

        public void InserirCategoria(string descricao)
        {
            Categoria categoria = new Categoria(descricao);
            categoriaDAO.Inserir(categoria);
        }

        public List<Categoria> ListarCategorias()
        {
            return categoriaDAO.Listar();
        }

        public Categoria? ListarCategoriaPorId(int id)
        {
            return categoriaDAO.Listar_Id(id);
        }

        public bool AtualizarCategoria(int id, string descricao)
        {
            Categoria categoria = new Categoria(descricao);
            categoria.Id = id;

            return categoriaDAO.Atualizar(categoria);
        }

        public bool ExcluirCategoria(int id)
        {
            return categoriaDAO.Excluir(id);
        }

        public void InserirProduto(string descricao, double preco, int estoque, int idCategoria)
        {
            Produto produto = new Produto(descricao, preco, estoque, idCategoria);
            produtoDAO.Inserir(produto);
        }

        public List<Produto> ListarProdutos()
        {
            return produtoDAO.Listar();
        }

        public Produto? ListarProdutoPorId(int id)
        {
            return produtoDAO.Listar_Id(id);
        }

        public bool AtualizarProduto(int id, string descricao, double preco, int estoque, int idCategoria)
        {
            Produto produto = new Produto(descricao, preco, estoque, idCategoria);
            produto.Id = id;

            return produtoDAO.Atualizar(produto);
        }

        public bool ExcluirProduto(int id)
        {
            return produtoDAO.Excluir(id);
        }
        public void ReajustarProdutos(double percentual)
        {
            foreach (Produto produto in produtoDAO.Listar())
            {
                double novoPreco = produto.Preco + (produto.Preco * percentual / 100);

                Produto atualizado = new Produto(
                    produto.Descricao,
                    novoPreco,
                    produto.Estoque,
                    produto.IdCategoria
                );

                atualizado.Id = produto.Id;

                produtoDAO.Atualizar(atualizado);
            }
        }
    }
}
