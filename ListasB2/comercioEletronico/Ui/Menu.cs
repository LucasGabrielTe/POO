
using System;
using comercioEletronico.Model;

namespace comercioEletronico.UI
{
    public class Menu
    {
        private comercioEletronico.Service.Service service =
            new comercioEletronico.Service.Service();


        public void MenuPrincipal()
        {
            Console.WriteLine("\n===== SISTEMA DE COMÉRCIO ELETRÔNICO =====");

            Console.WriteLine("\n1 - Inserir Cliente");
            Console.WriteLine("2 - Listar Clientes");
            Console.WriteLine("3 - Atualizar Cliente");
            Console.WriteLine("4 - Excluir Cliente");

            Console.WriteLine("\n5 - Inserir Categoria");
            Console.WriteLine("6 - Listar Categorias");
            Console.WriteLine("7 - Atualizar Categoria");
            Console.WriteLine("8 - Excluir Categoria");

            Console.WriteLine("\n9 - Inserir Produto");
            Console.WriteLine("10 - Listar Produtos");
            Console.WriteLine("11 - Atualizar Produto");
            Console.WriteLine("12 - Excluir Produto");

            Console.WriteLine("\n13 - Reajustar Preços");
            Console.WriteLine("0 - Finalizar");

            Console.Write("\nEscolha uma opção: ");
        }

        public void Main()
        {
            int opcao = -1;

            while (opcao != 0)
            {
                MenuPrincipal();

                int.TryParse(Console.ReadLine(), out opcao);

                switch (opcao)
                {
                    case 1: InserirCliente(); break;
                    case 2: ListarClientes(); break;
                    case 3: AtualizarCliente(); break;
                    case 4: ExcluirCliente(); break;

                    case 5: InserirCategoria(); break;
                    case 6: ListarCategorias(); break;
                    case 7: AtualizarCategoria(); break;
                    case 8: ExcluirCategoria(); break;

                    case 9: InserirProduto(); break;
                    case 10: ListarProdutos(); break;
                    case 11: AtualizarProduto(); break;
                    case 12: ExcluirProduto(); break;

                    case 13: ReajustarProdutos(); break;

                    case 0:
                        Console.WriteLine("Sistema finalizado!");
                        break;

                    default:
                        Console.WriteLine("Opção inválida!");
                        break;
                }
            }
        }

        public void InserirCliente()
        {
            Console.Write("Nome: ");
            string nome = Console.ReadLine() ?? "";

            Console.Write("Email: ");
            string email = Console.ReadLine() ?? "";

            Console.Write("Telefone: ");
            string fone = Console.ReadLine() ?? "";

            service.InserirCliente(nome, email, fone);

            Console.WriteLine("Cliente cadastrado!");
        }

        public void ListarClientes()
        {
            foreach (Cliente cliente in service.ListarClientes())
            {
                Console.WriteLine(
                    $"ID: {cliente.Id} | Nome: {cliente.Nome} | Email: {cliente.Email} | Telefone: {cliente.Fone}");
            }
        }

        public void AtualizarCliente()
        {
            Console.Write("ID do cliente: ");
            int id = int.Parse(Console.ReadLine() ?? "0");

            Console.Write("Novo nome: ");
            string nome = Console.ReadLine() ?? "";

            Console.Write("Novo email: ");
            string email = Console.ReadLine() ?? "";

            Console.Write("Novo telefone: ");
            string fone = Console.ReadLine() ?? "";

            if (service.AtualizarCliente(id, nome, email, fone))
                Console.WriteLine("Cliente atualizado!");
            else
                Console.WriteLine("Cliente não encontrado!");
        }

        public void ExcluirCliente()
        {
            Console.Write("ID do cliente: ");
            int id = int.Parse(Console.ReadLine() ?? "0");

            if (service.ExcluirCliente(id))
                Console.WriteLine("Cliente excluído!");
            else
                Console.WriteLine("Cliente não encontrado!");
        }

        public void InserirCategoria()
        {
            Console.Write("Descrição da categoria: ");
            string descricao = Console.ReadLine() ?? "";

            service.InserirCategoria(descricao);

            Console.WriteLine("Categoria cadastrada!");
        }

        public void ListarCategorias()
        {
            foreach (Categoria categoria in service.ListarCategorias())
            {
                Console.WriteLine(
                    $"ID: {categoria.Id} | Descrição: {categoria.Descricao}");
            }
        }

        public void AtualizarCategoria()
        {
            Console.Write("ID da categoria: ");
            int id = int.Parse(Console.ReadLine() ?? "0");

            Console.Write("Nova descrição: ");
            string descricao = Console.ReadLine() ?? "";

            if (service.AtualizarCategoria(id, descricao))
                Console.WriteLine("Categoria atualizada!");
            else
                Console.WriteLine("Categoria não encontrada!");
        }

        public void ExcluirCategoria()
        {
            Console.Write("ID da categoria: ");
            int id = int.Parse(Console.ReadLine() ?? "0");

            if (service.ExcluirCategoria(id))
                Console.WriteLine("Categoria excluída!");
            else
                Console.WriteLine("Categoria não encontrada!");
        }

        public void InserirProduto()
        {
            Console.Write("Descrição: ");
            string descricao = Console.ReadLine() ?? "";

            Console.Write("Preço: ");
            double preco = double.Parse(Console.ReadLine() ?? "0");

            Console.Write("Estoque: ");
            int estoque = int.Parse(Console.ReadLine() ?? "0");

            Console.Write("ID da categoria: ");
            int idCategoria = int.Parse(Console.ReadLine() ?? "0");

            service.InserirProduto(descricao, preco, estoque, idCategoria);

            Console.WriteLine("Produto cadastrado!");
        }

        public void ListarProdutos()
        {
            foreach (Produto produto in service.ListarProdutos())
            {
                Console.WriteLine(
                    $"ID: {produto.Id} | Descrição: {produto.Descricao} | Preço: R$ {produto.Preco:F2} | Estoque: {produto.Estoque} | Categoria: {produto.IdCategoria}");
            }
        }

        public void AtualizarProduto()
        {
            Console.Write("ID do produto: ");
            int id = int.Parse(Console.ReadLine() ?? "0");

            Console.Write("Nova descrição: ");
            string descricao = Console.ReadLine() ?? "";

            Console.Write("Novo preço: ");
            double preco = double.Parse(Console.ReadLine() ?? "0");

            Console.Write("Novo estoque: ");
            int estoque = int.Parse(Console.ReadLine() ?? "0");

            Console.Write("Novo ID da categoria: ");
            int idCategoria = int.Parse(Console.ReadLine() ?? "0");

            if (service.AtualizarProduto(id, descricao, preco, estoque, idCategoria))
                Console.WriteLine("Produto atualizado!");
            else
                Console.WriteLine("Produto não encontrado!");
        }

        public void ExcluirProduto()
        {
            Console.Write("ID do produto: ");
            int id = int.Parse(Console.ReadLine() ?? "0");

            if (service.ExcluirProduto(id))
                Console.WriteLine("Produto excluído!");
            else
                Console.WriteLine("Produto não encontrado!");
        }

        public void ReajustarProdutos()
        {
            Console.Write("Digite o percentual (positivo para aumento e negativo para promoção): ");

            double percentual = double.Parse(Console.ReadLine() ?? "0");

            service.ReajustarProdutos(percentual);

            Console.WriteLine("Preços reajustados!");
        }
    }
}
