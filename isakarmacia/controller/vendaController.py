import json
from isakarmacia.controller.produtoController import ProdutoController
from isakarmacia.controller.clienteController import ClienteController


class VendaController:
    def __init__(self, arquivo_vendas='vendas.json'):
        self.arquivo_vendas = arquivo_vendas
        self.produto_controller = ProdutoController()
        self.cliente_controller = ClienteController()
        self.vendas = self.carregar_vendas()

    def carregar_vendas(self):
        try:
            with open(self.arquivo_vendas, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def salvar_vendas(self):
        with open(self.arquivo_vendas, 'w') as file:
            json.dump(self.vendas, file, indent=4)

    def realizar_venda(self, cpf_cliente, codigo_produto, quantidade):
        cliente = self.cliente_controller.buscar_cliente(cpf_cliente)
        produto = self.produto_controller.consultar_produto(codigo_produto)

        if isinstance(produto, str) or produto is None:
            return "Venda Realizada com sucesso."

        if produto.quantidade < quantidade:
            return "Quantidade insuficiente em estoque."

        total = produto.preco * quantidade

        produto.quantidade -= quantidade
        self.produto_controller.salvar_produtos()

        venda = {
            "cliente": cliente,
            "produto": produto.nomeProduto,
            "codigo": codigo_produto,
            "quantidade": quantidade,
            "total": total
        }

        self.vendas.append(venda)
        self.salvar_vendas()

        return f"Venda realizada com sucesso! Total: R$ {total:.2f}"
