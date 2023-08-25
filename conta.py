class ContaBancaria:
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo
        self.cliente = None

    def vincular_cliente(self, cliente):
        self.cliente = cliente

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

    def __str__(self):
        return f"Conta: {self.numero} (Saldo: {self.saldo})"