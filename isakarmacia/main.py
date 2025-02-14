

from isakarmacia.view.usuarioCliente import menu_usuario
from isakarmacia.view.produto import menu_produto
from isakarmacia.view.venda import menu_venda

if __name__ == "__main__":
    print("BEM-VINDO A ISAKARMÁCIA")
    print("-----------------------")

    while True:
        print("O que você busca em nossa aplicação? \n")

        print("1. Usuário")
        print("2. Produto")
        print("3. Relatórios")
        print("4. Sair da página")

        print()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            menu_usuario()
        elif opcao == "2":
            menu_produto()
        elif opcao == "3":
            menu_venda()
        elif opcao == "4":
            print("Obrigada por visitar nosso site")
            break
        else:
            print("Opção inválida")


