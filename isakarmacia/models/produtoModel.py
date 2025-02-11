
class Produto:
    def __init__(self, nomeProduto, codigo, preco, quantidade):
        self.nome = nomeProduto
        self.codigo = codigo
        self.preco = preco
        self.quantidade = quantidade


    def exibir_dados_do_produto(self):
        return f"\n Nome do produto: {self.nome}\n Código do produto: {self.codigo}\n Preço do produto: {self.preco}\n Quantidade do produto no estoque {self.quantidade}"