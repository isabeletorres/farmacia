from isakarmacia.controller.vendaController import VendaController


def menu_venda():
    venda_controller = VendaController()

    while True:
        print("\n1. Realizar Venda\n2. Listar Vendas\n3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cpf = input("CPF do cliente: ")
            codigo = input("Código do produto: ")
            quantidade = int(input("Quantidade: "))
            print(venda_controller.realizar_venda(cpf, codigo, quantidade))

        elif opcao == "2":
            print("\nLista de Vendas:")
            for venda in venda_controller.vendas:
                print(venda)

        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")