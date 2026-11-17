using System.Collections.Generic;
using System.Linq;
using comercioEletronico.Model;

namespace comercioEletronico.DAO
{
    public class ClienteDAO
    {
        private List<Cliente> clientes = new List<Cliente>();
        private int proximoId = 1;

        public void Inserir(Cliente cliente)
        {
            cliente.Id = proximoId;
            proximoId++;

            clientes.Add(cliente);

        }

         public List<Cliente> Listar()
        {
            return clientes;
        }

        public Cliente? Listar_Id(int id)
        {
            return clientes.FirstOrDefault(c => c.Id == id);
        }

        public bool Atualizar(Cliente cliente)
        {
            Cliente? existente = Listar_Id(cliente.Id);

            if (existente == null)
                return false;

            existente.Nome = cliente.Nome;
            existente.Email = cliente.Email;
            existente.Fone = cliente.Fone;

            return true;
        }

        public bool Excluir(int id)
        {
            Cliente? cliente = Listar_Id(id);

            if (cliente == null)
                return false;

            clientes.Remove(cliente);

            return true;
        }
    }
}
    
