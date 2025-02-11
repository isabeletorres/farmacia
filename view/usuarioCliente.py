from controller.clienteController import ClienteController

def menu_cadastro_cliente():
    cliente_controller = ClienteController()

    while True:
        print("\n1. Cadastrar Cliente\n2. Listar Clientes\n3. Buscar Cliente\n4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            print(cliente_controller.cadastrar_cliente(nome, cpf, telefone))

        elif opcao == "2":
            print("\nLista de Clientes:")
            for cliente in cliente_controller.listar_clientes():
                print(cliente)

        elif opcao == "3":
            cpf = input("Digite o CPF do cliente: ")
            print(cliente_controller.buscar_cliente(cpf))

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

