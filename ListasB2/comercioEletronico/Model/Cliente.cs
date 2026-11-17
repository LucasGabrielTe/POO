using System.ComponentModel.DataAnnotations;

namespace comercioEletronico.Model
{
    public class Cliente
    {
        public int Id {get; set; }
        public string Nome {get; set; }
        public string Email {get; set; }
        public string Fone {get; set; }

        public Cliente ( string nome, string email, string fone)
        {
            Nome = nome;
            Email = email;
            Fone = fone;
        }
    }
}