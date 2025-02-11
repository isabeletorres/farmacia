
class Client:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone


    def exibir_dados(self):
        return f"Nome: {self.nome}\n CPF: {self.cpf}\n Telefone: {self.telefone}"
