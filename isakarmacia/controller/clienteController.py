import json
import os
from isakarmacia.models.clienteModel import Client

class ClienteController:
    def __init__(self, arquivo="clientes.json"):
        self.arquivo = arquivo
        self.clientes = self.carregar_dados()

    def salvar_dados(self):
        with open(self.arquivo, "w") as f:
            json.dump([vars(cliente) for cliente in self.clientes], f, indent=4)

    def carregar_dados(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r") as f:
                dados = json.load(f)
                return [Client(**cliente) for cliente in dados]
        return []

    def cadastrar_cliente(self, nome, cpf, telefone):
        novo_cliente = Client(nome, cpf, telefone)
        self.clientes.append(novo_cliente)
        self.salvar_dados()
        return "Cliente cadastrado com sucesso!"

    def listar_clientes(self):
        return [cliente.exibir_dados() for cliente in self.clientes]

    def buscar_cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente.exibir_dados()
        return "Cliente não encontrado."

    def deletar_cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                self.clientes.remove(cliente)
                self.salvar_dados()
                return f"Cliente com CPF {cpf} deletado com sucesso!"
        return "Cliente não encontrado."
