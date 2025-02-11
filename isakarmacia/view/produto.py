from isakarmacia.controller.produtoController import ProdutoController

def menu_produto():
    produto_controller = ProdutoController()

    print("Bem-Vindo à Área de Produto!")
    print("O que você deseja fazer?")
    print()

    while True:
        print("\n1. Cadastrar produto\n2. Listar Produtos\n3. Buscar Produto\n4. Deletar Produto\n5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            codigo = input("Código do produto: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            produto_controller.cadastrar_produto(codigo, nome, preco, quantidade)

        elif opcao == "2":
            print("\nLista de Produtos:")
            for produto in produto_controller.produtos.values():
                print(produto.exibir_dados_do_produto())

        elif opcao == "3":
            codigo = input("Código do produto: ")
            print(produto_controller.consultar_produto(codigo))

        elif opcao == "4":
            codigo = input("Código do produto: ")
            print(produto_controller.excluir_produto(codigo))
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida")
