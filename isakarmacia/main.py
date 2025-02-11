

from isakarmacia.view.usuarioCliente import menu_cadastro_cliente

if __name__ == "__main__":
    print("BEM-VINDO A ISAKARMÁCIA")
    print("-----------------------")
    print("O que você busca em nossa aplicação? \n")

    print("1. Usuário")
    print("2. Produto")
    print("3. Relatórios")

    print()

    opcao = input("Escolha uma opção: ")
    if opcao == "1":

        menu_cadastro_cliente()
