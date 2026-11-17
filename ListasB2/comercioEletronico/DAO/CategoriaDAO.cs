using System.Collections.Generic;
using System.Linq;
using comercioEletronico.Model;

namespace comercioEletronico.DAO
{
    public class CategoriaDAO
    {
        private List<Categoria> categorias = new List<Categoria>();
        private int proximoId = 1;

        public void Inserir(Categoria categoria)
        {
            categoria.Id = proximoId;
            proximoId++;
            categorias.Add(categoria);
        }

        public List<Categoria> Listar()
        {
            return categorias;
        }

        public Categoria? Listar_Id(int id)
        {
            return categorias.FirstOrDefault(c => c.Id == id);
        }

        public bool Atualizar(Categoria categoria)
        {
            Categoria? existente = Listar_Id(categoria.Id);

            if (existente == null)
                return false;

            existente.Descricao = categoria.Descricao;
            return true;
        }

        public bool Excluir(int id)
        {
            Categoria? categoria = Listar_Id(id);

            if (categoria == null)
                return false;

            categorias.Remove(categoria);
            return true;
        }
    }
}