class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.conta = None

    def vincular_conta(self, conta):
        self.conta = conta

    def __str__(self):
        return f"Cliente: {self.nome} (CPF: {self.cpf})"