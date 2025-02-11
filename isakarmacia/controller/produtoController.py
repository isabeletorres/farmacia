import json
from isakarmacia.models.produtoModel import Produto
class ProdutoController:
    def __init__(self, arquivo_json='produtos.json'):
        self.arquivo_json = arquivo_json
        self.produtos = self.carregar_produtos()

    def carregar_produtos(self):
        try:
            with open(self.arquivo_json, 'r') as file:
                produtos = json.load(file)
                return {produto['codigo']: Produto(nomeProduto=produto['nome'], codigo=produto['codigo'], preco=produto['preco'], quantidade=produto['quantidade']) for produto in produtos}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def salvar_produtos(self):
        with open(self.arquivo_json, 'w') as file:
            produtos = [produto.__dict__ for produto in self.produtos.values()]
            json.dump(produtos, file, indent=4)

    def adicionar_produto(self, produto):
        if produto.codigo in self.produtos:
            print("Produto com este código já existe!")
        else:
            self.produtos[produto.codigo] = produto
            self.salvar_produtos()
            print("Produto adicionado com sucesso!")


    def excluir_produto(self, codigo):
        if codigo in self.produtos:
            del self.produtos[codigo]
            self.salvar_produtos()
            print("Produto excluído com sucesso!")
        else:
            print("Produto não encontrado!")

    def consultar_produto(self, codigo):
        if codigo in self.produtos:
            return self.produtos[codigo].exibir_dados_do_produto()
        else:
            print("Produto não encontrado!")
            return None

    def cadastrar_produto(self, codigo, nomeProduto, preco, quantidade):
        if codigo in self.produtos:
            print("Produto com este código já existe!")
        else:
            produto = Produto(nomeProduto=nomeProduto, codigo=codigo, preco=preco, quantidade=quantidade)
            self.adicionar_produto(produto)